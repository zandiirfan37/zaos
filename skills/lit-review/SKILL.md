---
name: lit-review
description: Citation-grounded question answering over a curated LOCAL corpus of papers and notes. Use for "what does prior work say about X" with traceable references. Not general web research, not a knowledge store, not manuscript authority.
---

# Literature review (citation-grounded, local corpus)

`scripts/litqa.py` answers a question using only a directory of `.pdf` / `.md` /
`.txt` files you curate. Retrieval is TF-IDF (scikit-learn, CPU). Synthesis
defaults to the `claude` CLI — **no API key, no model download**, same auth as
`.agents/eval/`. An opt-in `--synthesizer codex` fallback exists for an
authenticated Codex environment, but is not the default because its agent-startup
token overhead is materially higher for short, bounded answers.

Every claim in the answer carries an `[E#]` citation to a corpus excerpt, or the
tool returns `INSUFFICIENT_CORPUS`. A citation that doesn't map to a retrieved
excerpt is reported as `UNGROUNDED_CITATION` (exit 1).

## Use

```bash
# review corpus health first — flags garbled PDF extraction
uv run .agents/skills/lit-review/scripts/litqa.py index research/literature/corpus

uv run .agents/skills/lit-review/scripts/litqa.py ask research/literature/corpus \
  "What conditions must hold for compressed sensing recovery to succeed?" \
  --k 6 --out research/literature/answers/cs-conditions.md

# When the Claude CLI is unavailable in an otherwise authenticated Codex setup:
uv run .agents/skills/lit-review/scripts/litqa.py ask research/literature/corpus \
  "What conditions must hold for compressed sensing recovery to succeed?" \
  --synthesizer codex --k 6 --out research/literature/answers/cs-conditions.md
```

Exit `0` = grounded answer. `1` = INSUFFICIENT_CORPUS or ungrounded citation.
`2` = corpus/usage error.

## Corpus discipline

- **Prefer `.md`.** `index` reports `extraction_quality` per file; anything below
  ~0.75 (common for math/scanned PDFs — number-for-letter substitution) must be
  converted to `.md` and spot-checked before it is trusted. `litqa` reads garbled
  text just as happily as good text.
- The corpus lives in the **owning project**, gitignored:
  `projects/<p>/research/literature/corpus/`. It is not a global store and not
  shared between projects. Full layout, provenance ledger, and the paper-q1 pilot
  checklist: `references/corpus-setup.md`.
- Copyright: only put files you are licensed to hold (open-access, your own, or
  institutionally licensed). Do not have the agent bulk-download paywalled PDFs.

## Output is evidence, not authority

Answers go to `research/literature/answers/*.md` as **evidence artifacts**. They
are never a contract, never manuscript text, and never cited in the paper until a
human has checked each `[E#]` against the source. A derived answer must not become
project authority — Git, contracts, and the corpus itself outrank it.

## Limits / when to escalate

- TF-IDF retrieval is keyword-ish; a question phrased far from the corpus's
  vocabulary may miss relevant chunks (raise `--k`, or rephrase).
- No multi-hop reasoning, no reranking, no cross-paper synthesis beyond what one
  retrieval pass surfaces.
- The Codex fallback reports elapsed time and, when available from the CLI,
  token use; it does **not** claim a monetary cost because the CLI does not
  provide a reliable cost field. Use it only as a bounded portability fallback.
- If the project needs agentic multi-hop literature search (contextual summaries,
  citation-graph traversal), that is **PaperQA2** — which needs an LLM API key +
  budget, a Human Lead decision. This skill is the lightweight, no-secrets tier.
