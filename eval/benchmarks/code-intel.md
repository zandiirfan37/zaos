# Code-intelligence tournament — benchmark contract

Question: **does an added code-intelligence tool beat the ZAOS baseline enough to
justify its complexity, and if so which tool becomes the one canonical owner?**

A baseline win is a valid, desirable outcome. The end state is one owner — or none.

## Target project

`projects/gradtime_v2` — 55 Python modules, ~9,400 lines, two packages
(`gradtime/` domain + `gradtime_ops/` ops) plus `app/`, `tests/`, and 15+
`workbench/NN_*/run_*.py` study scripts that import from `src/`. Import-resolved
navigation is genuinely non-trivial here: a symbol defined in `src/` is typically
used across `app/`, `tests/`, and many `workbench/` scripts, and `rg` scoped to
`src/` misses all of it.

## Arms

| arm | what | setup cost | run cost |
| --- | --- | --- | --- |
| **B0 baseline** (required) | `Read` + `Grep` + `Glob`, current ZAOS default | none | model reads files to disambiguate |
| **B1 jedi-helper** | a thin `code-nav` script wrapping `jedi` (find-def, find-refs, follow-import) | `uv run --with jedi`, ~6 s once | ~0 (CPU, local) |
| **B2 ast-grep** | structural pattern search (`ast-grep`/`sg`, single 52 MB binary) | download binary | ~0 |
| **B3 Serena** | LSP-backed semantic toolkit, runs as an MCP server / agent | pip + LSP server (pyright/jedi) + MCP wiring; RAM for the server | server process running |
| **B4 Codebase Memory / Graphify** | persistent code-graph index | index build + on-disk store + staleness handling | index refresh on code change |

Do **not** install B3/B4 until B0–B2 show the capability is worth the tournament.
This contract's initial run covered B0 vs B1 (see `INITIAL_RESULTS`).

## Benchmark tasks (build a ground-truth key for each by reading the code + jedi)

| # | capability | task on gradtime_v2 |
| --- | --- | --- |
| T1 | symbol discovery | where is the student-snapshot builder defined? |
| T2 | callers / references | every real call site of `snapshot_table` |
| T3 | dependency tracing | internal modules `gradtime_ops.recertification` depends on, 1 hop |
| T4 | data-flow | where the as-of / cutoff date enters snapshot feature computation |
| T5 | architectural navigation | the boundary/contract between `gradtime` and `gradtime_ops` |
| T6 | blast radius | files affected by changing `snapshot_table`'s signature (GT: 13) |
| T7 | semantic discovery | the code handling competing-risk / censoring in the hazard model |
| T8 | source-grounded explanation | how `gradtime_ops.parity` verifies parity, citing functions |

## Metrics (per task × arm)

| metric | how measured |
| --- | --- |
| correctness | graded 0/1 (or fractional recall) vs the ground-truth key, human-checked |
| source grounding | fraction of cited `file:line` that actually contain the claim |
| context / tokens | `usage.input_tokens` + `usage.output_tokens` from `claude -p --output-format json` |
| tool calls | `num_turns` |
| latency | wall time |
| setup / indexing cost | one-time seconds + disk |
| RAM / disk / runtime burden | RSS of any server; index size on disk |
| freshness after change | edit a symbol, re-ask T2/T6 without re-indexing — stale? |
| Claude / Codex portability | does the arm work under Codex's sandbox (network/exec limits)? |
| maintenance | new dependency? version pinning? upstream churn? |

## Run protocol

For each (task, arm): one `claude -p --model sonnet --output-format json
--allowedTools <arm tools> --add-dir <project>`, prompt = task + arm-specific tool
hint. Capture the JSON. Grade correctness against the key. Repeat once on `haiku`
for the attribution signal (does the tool help a weaker agent more — the Wave-1
eval-harness lesson). Keep every raw transcript.

## Decision rule

- If **B0 wins or ties** on correctness at ≤1.3× the token/time cost of the best
  tool → **adopt nothing**; record the negative result.
- If a tool wins correctness *or* cuts tokens/turns ≥30% consistently → it advances.
- Among advancing tools, the **canonical owner** is the one with the best
  correctness-per-complexity: prefer B1 (no binary, no server) unless B2/B3
  demonstrably do something B1 cannot (structural rewrite; cross-language; or an
  agent-usability gain a plain script can't match).
- One owner, wrapped as a `code-nav` skill (CLI + checklist, like `browser-qa`).
  No MCP unless a measured agent-usability gain requires it.

## Initial run (2026-09-06): B0 vs B1

See `.runtime/eval/code-intel/INITIAL_RESULTS.md`. On T6 (blast radius): B1 got
13/13 exact at −34% output tokens / −25% time / −20% cost / −20% turns vs B0's
12/13. Mechanical find-references showed `rg` scoped to `src/` misses 8–24 real
sites per symbol. **Signal: a code-intelligence tool earns the next round.** Next
step: build the `code-nav` jedi wrapper as a proper skill, then run the full T1–T8
grid for B0 / B1 / B2, and only then decide whether B3 (Serena) is worth testing.
