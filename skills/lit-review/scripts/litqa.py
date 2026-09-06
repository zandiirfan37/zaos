# /// script
# requires-python = ">=3.11"
# dependencies = ["pypdf>=6", "scikit-learn>=1.4", "numpy>=1.26"]
# ///
"""ZAOS lit-review — citation-grounded Q&A over a LOCAL corpus of papers/docs.

No API key. Retrieval is TF-IDF (scikit-learn, CPU); synthesis is the `claude`
CLI (subscription auth, same as the eval harness). Every claim in the answer is
tied to a corpus excerpt, or the tool says INSUFFICIENT_CORPUS.

    uv run .agents/skills/lit-review/scripts/litqa.py ask <corpus_dir> "question" \
        --k 8 --out answer.md

Corpus = a directory of .pdf / .md / .txt files. Output = a markdown answer with
a References block (file + page/chunk) and a JSON report to stdout. It is
EVIDENCE — write it into the owning project's evidence/ or research/, never a
contract, never manuscript text without human verification.

Exit 0 = answered with grounded citations. 1 = INSUFFICIENT_CORPUS or a
citation failed to ground. 2 = usage/corpus error.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

logging.getLogger("pypdf").setLevel(logging.ERROR)
logging.getLogger("fontTools").setLevel(logging.ERROR)

ZANDI = Path(__file__).resolve().parents[4]
CLAUDE_CONFIG = ZANDI / ".runtime" / "engines" / "claude"


def extract(path: Path) -> list[tuple[int, str]]:
    """Return [(page_or_block_no, text)] for one file."""
    if path.suffix.lower() == ".pdf":
        from pypdf import PdfReader
        out = []
        for i, pg in enumerate(PdfReader(str(path)).pages, 1):
            t = (pg.extract_text() or "").strip()
            if t:
                out.append((i, t))
        return out
    text = path.read_text(errors="replace")
    # split markdown/text into ~800-word blocks
    words = text.split()
    blocks, cur, n = [], [], 1
    for w in words:
        cur.append(w)
        if len(cur) >= 800:
            blocks.append((n, " ".join(cur))); cur = []; n += 1
    if cur:
        blocks.append((n, " ".join(cur)))
    return blocks


def chunk(pages: list[tuple[int, str]], target_words: int = 220) -> list[tuple[int, str]]:
    chunks = []
    for pageno, text in pages:
        paras = re.split(r"\n\s*\n", text)
        buf: list[str] = []
        for para in paras:
            buf.append(para.strip())
            if sum(len(x.split()) for x in buf) >= target_words:
                chunks.append((pageno, " ".join(buf))); buf = []
        if buf:
            chunks.append((pageno, " ".join(buf)))
    return [(p, c) for p, c in chunks if len(c.split()) >= 15]


_WORD = re.compile(r"[A-Za-z]{2,}")


def extraction_quality(text: str) -> float:
    """Rough 0..1 score: fraction of tokens that look like real words."""
    toks = text.split()
    if not toks:
        return 0.0
    wordish = sum(1 for t in toks if _WORD.search(t) and sum(c.isdigit() for c in t) <= len(t) // 3)
    return round(wordish / len(toks), 3)


def build_corpus(corpus_dir: Path) -> tuple[list[dict], list[dict]]:
    files = sorted(
        [p for p in corpus_dir.rglob("*") if p.suffix.lower() in (".pdf", ".md", ".txt")
         and not p.name.startswith(".")]
    )
    if not files:
        sys.exit(f"[2] no .pdf/.md/.txt files in {corpus_dir}")
    docs, file_report = [], []
    for f in files:
        try:
            pages = extract(f)
        except Exception as e:  # noqa: BLE001
            file_report.append({"file": f.name, "status": f"unreadable: {e}"})
            continue
        full = " ".join(t for _, t in pages)
        q = extraction_quality(full)
        n0 = len(docs)
        for pageno, text in chunk(pages):
            docs.append({"id": f"{f.stem}#p{pageno}#{len(docs)}",
                         "file": str(f.relative_to(corpus_dir)), "page": pageno, "text": text})
        file_report.append({
            "file": str(f.relative_to(corpus_dir)), "chars": len(full),
            "chunks": len(docs) - n0, "extraction_quality": q,
            "status": "OK" if q >= 0.75 else "LOW_QUALITY_EXTRACTION -> convert to .md and verify",
        })
    if not docs:
        sys.exit("[2] corpus produced no readable chunks")
    return docs, file_report


def retrieve(docs: list[dict], question: str, k: int) -> list[dict]:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import linear_kernel
    corpus = [d["text"] for d in docs]
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_df=0.85, sublinear_tf=True)
    m = vec.fit_transform(corpus + [question])
    sims = linear_kernel(m[-1], m[:-1]).ravel()
    order = sims.argsort()[::-1][:k]
    return [{**docs[i], "score": round(float(sims[i]), 4)} for i in order if sims[i] > 0]


SYNTH = """You are a scientific literature assistant. Answer the QUESTION using ONLY the
numbered EXCERPTS below. Rules:
- Every factual sentence must end with a citation like [E3] or [E1][E4] naming the
  excerpt(s) it came from. No citation = delete the sentence.
- Do not use outside knowledge. Do not infer beyond the excerpts.
- If the excerpts are insufficient to answer, reply with exactly:
  INSUFFICIENT_CORPUS
  then one line naming what is missing. Nothing else.
- Be concise: 4-10 sentences, then a "Key points" list of 2-5 bullets (each cited).

QUESTION: {question}

EXCERPTS:
{excerpts}
"""


def _prompt(question: str, hits: list[dict]) -> str:
    ex = "\n\n".join(
        f"[E{i+1}] (file: {h['file']}, page {h['page']})\n{h['text'][:1600]}"
        for i, h in enumerate(hits)
    )
    return SYNTH.format(question=question, excerpts=ex)


def synth_claude(prompt: str, timeout: int, max_budget: float) -> dict:
    env = {**os.environ, "CLAUDE_CONFIG_DIR": str(CLAUDE_CONFIG)}
    with tempfile.TemporaryDirectory(prefix="litqa-") as cwd:
        p = subprocess.run(
            ["claude", "-p", "--model", "sonnet", "--output-format", "json",
             "--max-budget-usd", str(max_budget), "--allowedTools", "none"],
            input=prompt, capture_output=True, text=True, timeout=timeout,
            env={**env, "PWD": cwd}, cwd=cwd,
        )
    if p.returncode != 0:
        sys.exit(f"[2] claude failed: {(p.stderr or p.stdout)[:500]}")
    d = json.loads(p.stdout)
    return {"text": d.get("result", "") or "", "cost_usd": d.get("total_cost_usd"),
            "duration_ms": d.get("duration_ms"), "tokens": None,
            "synthesizer": "claude"}


def synth_codex(prompt: str, timeout: int) -> dict:
    """Run an authenticated Codex CLI synthesis without tool access.

    Codex does not expose a reliable monetary-cost field, so it reports an
    observed token count when the CLI emits one. This is opt-in because Codex
    has higher startup overhead than Claude for short, bounded answers.
    """
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="litqa-codex-") as cwd:
        answer_path = Path(cwd) / "answer.md"
        p = subprocess.run(
            ["codex", "exec", "--ephemeral", "--skip-git-repo-check",
             "--sandbox", "read-only", "-C", cwd,
             "--output-last-message", str(answer_path), prompt],
            capture_output=True, text=True, timeout=timeout, cwd=cwd,
        )
        if p.returncode != 0 or not answer_path.is_file():
            sys.exit(f"[2] codex failed: {(p.stderr or p.stdout)[:500]}")
        text = answer_path.read_text(errors="replace")
    token_match = re.search(r"tokens used\s*\n\s*([\d,]+)", p.stderr + "\n" + p.stdout)
    return {"text": text, "cost_usd": None,
            "duration_ms": round((time.monotonic() - started) * 1000),
            "tokens": int(token_match.group(1).replace(",", "")) if token_match else None,
            "synthesizer": "codex"}


def synth(question: str, hits: list[dict], timeout: int, max_budget: float,
          synthesizer: str) -> dict:
    prompt = _prompt(question, hits)
    if synthesizer == "claude":
        return synth_claude(prompt, timeout, max_budget)
    return synth_codex(prompt, timeout)


def ground_check(answer: str, hits: list[dict]) -> tuple[bool, list[str]]:
    cited = set(int(x) for x in re.findall(r"\[E(\d+)\]", answer))
    valid = set(range(1, len(hits) + 1))
    bad = sorted(cited - valid)
    has_any = bool(cited)
    return (has_any and not bad), [f"E{b} cited but only {len(hits)} excerpts" for b in bad] + \
        ([] if has_any else ["no [E#] citations in answer"])


def main() -> int:
    ap = argparse.ArgumentParser(prog="litqa")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("ask")
    a.add_argument("corpus"); a.add_argument("question")
    a.add_argument("--k", type=int, default=8)
    a.add_argument("--out", help="write the markdown answer here")
    a.add_argument("--timeout", type=int, default=180)
    a.add_argument("--max-budget", type=float, default=0.40)
    a.add_argument("--synthesizer", choices=("claude", "codex"), default="claude",
                   help="Claude is the lightweight default; Codex is an opt-in portability fallback.")
    i = sub.add_parser("index"); i.add_argument("corpus")
    args = ap.parse_args()

    corpus_dir = Path(args.corpus).resolve()
    if not corpus_dir.is_dir():
        sys.exit(f"[2] not a directory: {corpus_dir}")
    docs, file_report = build_corpus(corpus_dir)

    if args.cmd == "index":
        print(json.dumps({"corpus": str(corpus_dir), "files": file_report,
                          "n_files": len(file_report), "n_chunks": len(docs)}, indent=2))
        return 0

    hits = retrieve(docs, args.question, args.k)
    if not hits:
        if args.out:
            Path(args.out).write_text(f"# {args.question}\n\nINSUFFICIENT_CORPUS\nNo corpus chunk matched the question.\n")
        print(json.dumps({"question": args.question, "corpus": str(corpus_dir),
                          "n_chunks_indexed": len(docs), "k": args.k, "corpus_files": file_report,
                          "retrieved": [], "status": "INSUFFICIENT_CORPUS",
                          "grounding_problems": ["no chunk matched the question"],
                          "cost_usd": 0.0, "duration_ms": 0, "out": args.out}, indent=2))
        return 1
    s = synth(args.question, hits, args.timeout, args.max_budget, args.synthesizer)
    answer = s["text"].strip()
    insufficient = answer.startswith("INSUFFICIENT_CORPUS")
    grounded, problems = (False, ["insufficient"]) if insufficient else ground_check(answer, hits)

    refs = "\n".join(
        f"- [E{i+1}] {h['file']} p.{h['page']} (tfidf {h['score']})"
        for i, h in enumerate(hits)
    )
    md = f"# {args.question}\n\n{answer}\n\n## References (corpus-grounded)\n{refs}\n"
    if args.out:
        Path(args.out).write_text(md)

    report = {
        "question": args.question, "corpus": str(corpus_dir),
        "n_chunks_indexed": len(docs), "k": args.k,
        "corpus_files": file_report,
        "retrieved": [{"id": h["id"], "file": h["file"], "page": h["page"], "score": h["score"]} for h in hits],
        "status": "INSUFFICIENT_CORPUS" if insufficient else ("GROUNDED" if grounded else "UNGROUNDED_CITATION"),
        "grounding_problems": problems,
        "cost_usd": s["cost_usd"], "duration_ms": s["duration_ms"],
        "tokens": s["tokens"], "synthesizer": s["synthesizer"],
        "out": args.out,
    }
    print(json.dumps(report, indent=2))
    return 0 if (grounded and not insufficient) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
