# ZAOS engine tools

Engine-neutral command-line tools for ZAOS control-plane work. Callable
identically from the Codex and Claude routes. Nothing here loads during normal
work — a tool runs only when an executor invokes it.

| Tool | What it does |
| --- | --- |
| [`zaos-doctor`](zaos-doctor) | one-shot **read-only, advisory** diagnostic: git transaction-capability · RUNTIME_CONTRACT reconcile (EXPECTED vs `docker ps`) · stale/orphan background-job heuristic · resource headroom · leak-safe secret validation · container clock skew · workbench→production promotion guard · capability-reuse hint |

## zaos-doctor

```
.agents/engines/tools/zaos-doctor [--project <root>] \
    [--mode READ_ONLY|NORMAL_PROJECT_MUTATION|ZAOS_MAINTENANCE] \
    [--groups git,runtime,job,resource,secret,clock,promotion,capability]
.agents/engines/tools/zaos-doctor --secret-file <path>   # leak-safe single-file scan
.agents/engines/tools/zaos-doctor --capability <name>    # bounded local prior-art hint
.agents/engines/tools/zaos-doctor --assert-readonly      # static self-check
```

`--project` defaults to the CWD's git toplevel. `--mode` tunes only the
git-writability expectation. Output is line-oriented (`PASS:` / `INFO:` /
`WARN:` / `FAIL_CHECK:` / `SKIP:`) followed by a one-line summary. Exit code:
`0` clean · `1` ≥1 WARN · `2` ≥1 FAIL_CHECK · `3` doctor crashed.

### Contract

`zaos-doctor` is:

- **read-only** — never writes, moves, or deletes a file; never runs a git
  write or clears a lock; never starts/stops/kills a container, process, or
  service; never reads or prints a secret value; never installs; never touches
  the network.
- **advisory** — a preflight and reconciliation aid. It *reports*; the executor
  and the Human Lead decide.
- **NOT** a lifecycle authority, **NOT** a gate, **NOT** permission to mutate,
  **NOT** a replacement for executor judgement, **NOT** a source of canonical
  project truth.

**The exit code is information, never a block.** An executor that sees exit `1`
reads the lines and decides; it does not halt. A `WARN` is advice — it does not
by itself trigger any canonical hard block. An independently defined canonical
hard block, where one exists, is triggered by the underlying situation, not by
this tool. `zaos-doctor` does not define a new hard-block class.

Current project / git truth still comes from live inspection and the project's
own `PROJECT_STATE.md` and contracts — not from doctor output.

### Promotion guard

For Python production sources (`src contracts pipeline app lib`), an embedded
`ast` check flags only real `import` of a workbench/legacy module and
non-docstring path-shaped string literals pointing at `00_workbench/` /
`workbench/` / a legacy project dir. Docstrings, comments, and `test_*` files
are ignored. Non-Python files get a narrowed comment-skipping grep. An
unparseable production file falls back to a comment-stripped line scan. A
project with a documented, hash-locked exception lists it in
`<project>/tools/promotion-allowlist.txt`.

### Tests

`tests/run_tests.sh` — self-contained regression + adversarial suite. Bounded
waits only, owns and cleans its own scratch, no orphan shells, no dependency on
any project. Run: `bash .agents/engines/tools/tests/run_tests.sh`.

### Provenance

Prototyped and pilot-proven as `zaos-doctor v0` in
`projects/06_zaos_control_plane/tools/` across four real `05_chatbot_rag`
sprints (Pilots #1–#4), then promoted here. The prototype copy and its pilot
evidence remain in project 06 as historical record. `zaos-handoff` and
`ORCHESTRATOR_PRIMER` were **not** promoted and remain prototypes in project 06.

Known validation gap carried forward: the JOB group's stall/orphan heuristic
has fixture coverage only — no pilot sprint has yet armed a real long-running
background job. A genuine field exercise is still owed (expected at
`05_chatbot_rag` Stage 05).
