#!/usr/bin/env python3
"""ZAOS evaluation harness — behavioural + static checks for skills and doctrine.

Stdlib only. Runs on demand; nothing here is loaded during normal work.

    uv run .agents/eval/zaos_eval.py run ml-research
    uv run .agents/eval/zaos_eval.py run ml-research --ab            # skill vs baseline
    uv run .agents/eval/zaos_eval.py run ml-research --engine both
    uv run .agents/eval/zaos_eval.py run ml-research --skill-file /tmp/mutated.md
    uv run .agents/eval/zaos_eval.py list ml-research

Cases live next to the capability: .agents/skills/<skill>/eval/cases.toml
Evidence is written under .runtime/eval/<skill>/<utc>/  (disposable, not canonical).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import tomllib
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]              # ZAOS framework root
SKILLS = ROOT / "skills"
EVIDENCE_ROOT = Path(os.environ.get("ZAOS_EVAL_ROOT", Path.home() / ".local" / "state" / "zaos" / "eval"))
CACHE_DIR = EVIDENCE_ROOT / ".cache"
CLAUDE_CONFIG = Path(os.environ.get("ZAOS_RUNTIME_ROOT", Path.home() / ".local" / "state" / "zaos" / "engines")) / "claude"
CODEX_HOME = Path(os.environ.get("ZAOS_RUNTIME_ROOT", Path.home() / ".local" / "state" / "zaos" / "engines")) / "codex"

SCHEMA_VERSIONS = {"1"}
KINDS = {"behavioural", "behavioral", "static", "activation"}


# ----------------------------- engine invocation -----------------------------

def _run(cmd: list[str], env: dict, timeout: int, stdin: str | None = None,
         cwd: str | None = None) -> tuple[int, str, str]:
    try:
        p = subprocess.run(
            cmd, env=env, input=stdin, capture_output=True, text=True,
            timeout=timeout, cwd=cwd,
        )
    except subprocess.TimeoutExpired:
        return 124, "", f"timeout after {timeout}s"
    return p.returncode, p.stdout, p.stderr


def call_claude(prompt: str, *, model: str, config_dir: Path, timeout: int,
                max_budget: float = 0.60) -> dict:
    env = {**os.environ, "CLAUDE_CONFIG_DIR": str(config_dir)}
    # prompt via stdin: --allowedTools is variadic and would eat a positional prompt.
    # run from an isolated tmp cwd so the agent cannot wander into project trees.
    with tempfile.TemporaryDirectory(prefix="zaos-eval-") as cwd:
        cmd = [
            "claude", "-p", "--model", model, "--output-format", "json",
            "--max-budget-usd", str(max_budget),
            "--add-dir", str(SKILLS),
            "--allowedTools", "Read", "Glob", "Grep",  # read-only; all else auto-denied under -p
        ]
        rc, out, err = _run(cmd, {**env, "PWD": cwd}, timeout, stdin=prompt, cwd=cwd)
    if rc != 0:
        return {"ok": False, "engine": "claude", "text": "", "error": (err or out)[:2000], "meta": {}}
    try:
        d = json.loads(out)
    except json.JSONDecodeError:
        return {"ok": False, "engine": "claude", "text": out, "error": "non-json output", "meta": {}}
    return {
        "ok": bool((d.get("result") or "").strip()) and d.get("subtype") != "error_max_budget",
        "engine": "claude",
        "text": d.get("result", "") or "",
        "error": None if (d.get("result") or "").strip() else f"no final text (subtype={d.get('subtype')}, stop={d.get('stop_reason')})",
        "meta": {
            "cost_usd": d.get("total_cost_usd"),
            "duration_ms": d.get("duration_ms"),
            "input_tokens": (d.get("usage") or {}).get("input_tokens"),
            "output_tokens": (d.get("usage") or {}).get("output_tokens"),
            "num_turns": d.get("num_turns"),
            "session_id": d.get("session_id"),
        },
    }


def call_codex(prompt: str, *, model: str, codex_home: Path, timeout: int) -> dict:
    env = {**os.environ, "CODEX_HOME": str(codex_home)}
    with tempfile.NamedTemporaryFile("w+", suffix=".txt", delete=False) as tf:
        last_msg = Path(tf.name)
    try:
        cmd = [
            "codex", "exec", "--ephemeral", "--skip-git-repo-check",
            "--sandbox", "read-only", "-C", str(ROOT), "-m", model,
            "-o", str(last_msg), prompt,
        ]
        rc, out, err = _run(cmd, env, timeout)
        text = last_msg.read_text() if last_msg.exists() else ""
        return {
            "ok": rc == 0 and bool(text.strip()),
            "engine": "codex",
            "text": text,
            "error": None if rc == 0 else (err or out)[:2000],
            "meta": {"raw_stdout_tail": out[-500:]},
        }
    finally:
        last_msg.unlink(missing_ok=True)


# ----------------------------- assertions -----------------------------

def _rx(pat: str) -> re.Pattern:
    return re.compile(pat, re.IGNORECASE | re.MULTILINE | re.DOTALL)


def apply_assertions(text: str, case: dict) -> list[dict]:
    checks: list[dict] = []
    for pat in case.get("assert_all", []):
        checks.append({"type": "all", "pattern": pat, "passed": bool(_rx(pat).search(text))})
    any_pats = case.get("assert_any", [])
    if any_pats:
        hit = any(_rx(p).search(text) for p in any_pats)
        checks.append({"type": "any", "pattern": " || ".join(any_pats), "passed": hit})
    for pat in case.get("assert_none", []):
        checks.append({"type": "none", "pattern": pat, "passed": not _rx(pat).search(text)})
    return checks


def judge(text: str, rubric: str, *, model: str, timeout: int) -> dict:
    prompt = (
        "You are a strict evaluation judge. Given a RUBRIC and an ANSWER, decide if the "
        "ANSWER satisfies the RUBRIC. Reply with a single line: `VERDICT: PASS` or "
        "`VERDICT: FAIL`, then one sentence of justification.\n\n"
        f"RUBRIC:\n{rubric}\n\nANSWER:\n{text[:6000]}\n"
    )
    r = call_claude(prompt, model=model, config_dir=CLAUDE_CONFIG, timeout=timeout, max_budget=0.30)
    verdict = _rx(r"VERDICT:\s*(PASS|FAIL)").search(r["text"] or "")
    return {
        "type": "judge", "rubric": rubric,
        "passed": bool(verdict and verdict.group(1).upper() == "PASS"),
        "raw": (r["text"] or "").strip()[:400],
        "cost_usd": r["meta"].get("cost_usd"),
    }


# ----------------------------- case execution -----------------------------

def build_prompt(case: dict, *, skill: str, skill_file: Path | None, arm: str) -> str:
    scenario = case["prompt"].strip()
    isolation = (
        "Treat the scenario as fully self-contained. Do NOT read project files, "
        "assume a specific project, or reference any repository. Answer only from "
        "the scenario"
    )
    if arm == "baseline":
        return f"{isolation} and general expertise.\n\nBe concrete and decisive; ~250 words.\n\n---\n{scenario}"
    target = skill_file if skill_file else (SKILLS / skill / "SKILL.md")
    return (
        f"Read `{target}` and, if it points you to one, at most the single most "
        f"relevant file in its `references/`. Apply that skill's method.\n"
        f"{isolation}, the skill, and general expertise.\n"
        f"Be concrete and decisive; ~250 words.\n\n---\n{scenario}"
    )


HARNESS_REV = "2"  # bump when engine invocation semantics change (invalidates cache)


def cache_key(engine: str, model: str, prompt: str, skill_file: Path | None) -> str:
    h = hashlib.sha256()
    h.update(HARNESS_REV.encode()); h.update(b"\0")
    h.update(engine.encode()); h.update(b"\0"); h.update(model.encode()); h.update(b"\0")
    h.update(prompt.encode())
    if skill_file and skill_file.exists():
        h.update(b"\0"); h.update(skill_file.read_bytes())
    return h.hexdigest()


def invoke(engine: str, prompt: str, *, model: str, skill_file: Path | None,
           timeout: int, use_cache: bool, max_budget: float = 0.60) -> dict:
    key = cache_key(engine, model, prompt, skill_file)
    cf = CACHE_DIR / f"{key}.json"
    if use_cache and cf.exists():
        d = json.loads(cf.read_text()); d["_cached"] = True; return d
    if engine == "claude":
        r = call_claude(prompt, model=model, config_dir=CLAUDE_CONFIG, timeout=timeout, max_budget=max_budget)
    elif engine == "codex":
        r = call_codex(prompt, model=("gpt-5.6-terra" if model == "sonnet" else model),
                       codex_home=CODEX_HOME, timeout=timeout)
    else:
        raise ValueError(engine)
    r["_cached"] = False
    if r["ok"]:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        cf.write_text(json.dumps(r, indent=1))
    return r


def run_case(case: dict, *, skill: str, engine: str, model: str, skill_file: Path | None,
             ab: bool, timeout: int, use_cache: bool, raw_dir: Path) -> dict:
    kind = case.get("kind", "behavioural")
    result = {"id": case["id"], "kind": kind, "engine": engine, "arms": {}}

    if kind == "static":
        result["arms"]["static"] = _static_case(skill, case, skill_file)
        result["passed"] = result["arms"]["static"]["passed"]
        return result

    if kind == "activation":
        # Test routing: read only the skills index, then self-select the right skill.
        prompt = (
            f"Read `{SKILLS / 'README.md'}` (the ZAOS skills routing index) and nothing "
            f"else. Then, for the task below, name which skill(s) apply and why, or say "
            f"none apply. Two or three sentences.\n\n---\n{case['prompt'].strip()}"
        )
        r = invoke(engine, prompt, model=model, skill_file=None,
                   timeout=timeout, use_cache=use_cache,
                   max_budget=case.get('max_budget', 0.60))
        (raw_dir / f"{case['id']}.{engine}.route.txt").write_text(
            f"# prompt\n{prompt}\n\n# response (cached={r.get('_cached')})\n{r['text']}\n")
        checks = apply_assertions(r["text"], case) if r["ok"] else []
        arm_pass = r["ok"] and bool(checks) and all(c["passed"] for c in checks)
        result["arms"]["route"] = {
            "ok": r["ok"], "error": r["error"], "cached": r.get("_cached"),
            "checks": checks, "passed": arm_pass, "meta": r.get("meta", {}),
            "response_chars": len(r["text"]),
        }
        result["passed"] = arm_pass
        return result

    arms = ["skill"] + (["baseline"] if ab else [])
    for arm in arms:
        prompt = build_prompt(case, skill=skill, skill_file=skill_file, arm=arm)
        r = invoke(engine, prompt, model=model, skill_file=(skill_file if arm == "skill" else None),
                   timeout=timeout, use_cache=use_cache,
                   max_budget=case.get('max_budget', 0.60))
        (raw_dir / f"{case['id']}.{engine}.{arm}.txt").write_text(
            f"# prompt\n{prompt}\n\n# response (cached={r.get('_cached')})\n{r['text']}\n"
        )
        checks = apply_assertions(r["text"], case) if r["ok"] else []
        jd = case.get("judge", {})
        if r["ok"] and jd.get("enabled"):
            checks.append(judge(r["text"], jd["rubric"], model=model, timeout=timeout))
        arm_pass = r["ok"] and bool(checks) and all(c["passed"] for c in checks)
        result["arms"][arm] = {
            "ok": r["ok"], "error": r["error"], "cached": r.get("_cached"),
            "checks": checks, "passed": arm_pass, "meta": r.get("meta", {}),
            "response_chars": len(r["text"]),
        }

    result["passed"] = result["arms"]["skill"]["passed"]
    if ab and "baseline" in result["arms"]:
        result["skill_lift"] = bool(result["arms"]["skill"]["passed"]
                                    and not result["arms"]["baseline"]["passed"])
    return result


def _static_case(skill: str, case: dict, skill_file: Path | None) -> dict:
    p = skill_file or (SKILLS / skill / "SKILL.md")
    txt = p.read_text() if p.exists() else ""
    checks = []
    fm = re.match(r"^---\n(.*?)\n---\n", txt, re.DOTALL)
    checks.append({"type": "frontmatter", "passed": bool(fm)})
    if fm:
        checks.append({"type": "has_name", "passed": "name:" in fm.group(1)})
        checks.append({"type": "has_description", "passed": "description:" in fm.group(1)})
    max_lines = case.get("max_lines", 200)
    checks.append({"type": f"body_<= {max_lines} lines",
                   "passed": txt.count("\n") <= max_lines})
    for pat in case.get("assert_all", []):
        checks.append({"type": "all", "pattern": pat, "passed": bool(_rx(pat).search(txt))})
    return {"checks": checks, "passed": all(c["passed"] for c in checks), "path": str(p)}


# ----------------------------- driver -----------------------------

def load_cases(skill: str) -> dict:
    cf = SKILLS / skill / "eval" / "cases.toml"
    if not cf.exists():
        sys.exit(f"no cases file: {cf}")
    data = tomllib.loads(cf.read_text())
    if str(data.get("schema_version")) not in SCHEMA_VERSIONS:
        sys.exit(f"unknown schema_version in {cf}")
    for c in data.get("case", []):
        if "id" not in c or "prompt" not in c and c.get("kind") != "static":
            sys.exit(f"case missing id/prompt: {c}")
        k = c.get("kind", "behavioural")
        if k not in KINDS:
            sys.exit(f"bad kind {k!r} in case {c.get('id')}")
    return data


def cmd_run(args) -> int:
    data = load_cases(args.skill)
    cases = data.get("case", [])
    if args.case:
        cases = [c for c in cases if c["id"] in args.case]
        if not cases:
            sys.exit(f"no case matched {args.case}")
    engines = ["claude", "codex"] if args.engine == "both" else [args.engine]
    skill_file = Path(args.skill_file).resolve() if args.skill_file else None

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = Path(args.out) if args.out else EVIDENCE_ROOT / args.skill / ts
    raw_dir = out_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for eng in engines:
        for c in cases:
            print(f"  [{eng}] {c['id']} ...", flush=True)
            results.append(run_case(
                c, skill=args.skill, engine=eng, model=args.model, skill_file=skill_file,
                ab=args.ab, timeout=args.timeout, use_cache=not args.no_cache, raw_dir=raw_dir,
            ))

    passed = sum(1 for r in results if r["passed"])
    lift = sum(1 for r in results if r.get("skill_lift"))
    def _armcost(a): return (a.get("meta") or {}).get("cost_usd") or 0
    cost = sum(_armcost(a) for r in results for a in r.get("arms", {}).values())
    new_cost = sum(_armcost(a) for r in results for a in r.get("arms", {}).values() if not a.get("cached"))
    summary = {
        "skill": args.skill, "utc": ts, "engines": engines, "ab": args.ab,
        "skill_file_override": str(skill_file) if skill_file else None,
        "total": len(results), "passed": passed, "failed": len(results) - passed,
        "skill_lift_cases": lift, "approx_cost_usd": round(cost, 4),
        "new_spend_usd": round(new_cost, 4),
        "results": results,
    }
    (out_dir / "results.json").write_text(json.dumps(summary, indent=2))
    (out_dir / "summary.md").write_text(render_md(summary))
    print("\n" + render_md(summary))
    print(f"\nevidence: {out_dir}")
    return 0 if passed == len(results) else 1


def render_md(s: dict) -> str:
    lines = [
        f"# ZAOS eval — {s['skill']}",
        "",
        f"- utc: `{s['utc']}`  engines: {', '.join(s['engines'])}  ab: {s['ab']}",
        f"- **{s['passed']}/{s['total']} passed**, {s['failed']} failed"
        + (f", {s['skill_lift_cases']} skill-lift" if s["ab"] else ""),
        f"- cost: ${s['approx_cost_usd']} recorded / ${s.get('new_spend_usd', s['approx_cost_usd'])} new this run"
        + (f"  |  skill override: `{s['skill_file_override']}`" if s["skill_file_override"] else ""),
        "",
        "| case | kind | engine | skill arm | baseline arm | lift |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for r in s["results"]:
        sk = r["arms"].get("skill") or r["arms"].get("static") or r["arms"].get("route") or {}
        bl = r["arms"].get("baseline", {})
        skc = "PASS" if sk.get("passed") else "FAIL"
        blc = ("PASS" if bl.get("passed") else "FAIL") if bl else "—"
        lift = "yes" if r.get("skill_lift") else ("—" if not s["ab"] else "no")
        lines.append(f"| {r['id']} | {r['kind']} | {r['engine']} | {skc} | {blc} | {lift} |")
    lines += ["", "## failing checks", ""]
    any_fail = False
    for r in s["results"]:
        for arm, a in r.get("arms", {}).items():
            for c in a.get("checks", []):
                if not c["passed"]:
                    any_fail = True
                    lines.append(f"- `{r['id']}` [{arm}] {c['type']}: `{c.get('pattern', c.get('rubric',''))[:120]}`")
            if a.get("error"):
                any_fail = True
                lines.append(f"- `{r['id']}` [{arm}] ENGINE ERROR: {str(a['error'])[:160]}")
    if not any_fail:
        lines.append("_none_")
    return "\n".join(lines) + "\n"


def cmd_list(args) -> int:
    data = load_cases(args.skill)
    print(f"# {args.skill}  (schema {data['schema_version']})")
    for c in data.get("case", []):
        print(f"  {c['id']:<38} {c.get('kind','behavioural'):<12} "
              f"all={len(c.get('assert_all',[]))} any={len(c.get('assert_any',[]))} "
              f"none={len(c.get('assert_none',[]))} judge={bool(c.get('judge',{}).get('enabled'))}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="zaos_eval")
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="run a skill's eval cases")
    r.add_argument("skill")
    r.add_argument("--engine", choices=["claude", "codex", "both"], default="claude")
    r.add_argument("--model", default="sonnet")
    r.add_argument("--ab", action="store_true", help="also run baseline (no-skill) arm; report skill lift")
    r.add_argument("--case", action="append", help="run only this case id (repeatable)")
    r.add_argument("--skill-file", help="evaluate this file instead of the skill's SKILL.md (regression sims)")
    r.add_argument("--no-cache", action="store_true")
    r.add_argument("--timeout", type=int, default=240)
    r.add_argument("--out", help="evidence dir (default .runtime/eval/<skill>/<utc>)")
    r.set_defaults(func=cmd_run)

    l = sub.add_parser("list", help="list a skill's eval cases")
    l.add_argument("skill")
    l.set_defaults(func=cmd_list)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
