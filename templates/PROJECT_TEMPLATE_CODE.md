# Project template — code / AI project

Minimal adaptable standard. Create only what the project needs; never scaffold
empty directories. Number human sequence; keep machine/semantic names stable.

## Root documents (3–7)

- `README.md` — what / why / quickstart. **Required.**
- `PROJECT_STATE.md` — single compact current-state artifact. **Required.**
- `AGENTS.md` — only when local rules genuinely diverge from `BIG_SOP.md`.
- `PROJECT_DIRECTION.md` / `DECISIONS.md` — only when earned.
- one domain-specific policy document — only when the domain requires it.
- machine manifests as required (`pyproject.toml`, `uv.lock`, `.gitignore`) —
  not counted as documentation.

## Zones

| Path | Purpose | Notes |
| --- | --- | --- |
| `00_workbench/` | unrestricted exploration: experiments, audits, patches, benchmarks, scratch, debug, temporary evidence, alternative implementations, migration attempts | canonical areas must not depend on it |
| `src/<pkg>/` | semantic importable modules | never numbered |
| `tests/` | test suite | preserve discovery: `test_*.py`; `test_NN_*` only inside an ordered suite |
| `pipeline/` or numbered stage dirs | reproducible ordered workflow | `NN_` prefixes for human sequence; must not read `00_workbench/` |
| `config/`, `contracts/` | configuration, machine contracts | contract filenames are machine names — not numbered |
| `evidence/`, `deliverables/`, `data/`, `runtime/` | verification artifacts, outputs, inputs, disposable local state | only when needed |

## Promotion

Understand the winning experiment → rewrite/refactor it clean into the canonical
area → verify proportionally → update `PROJECT_STATE.md`. Do not move messy
workbench artifacts verbatim into production; the workbench artifact may stay as
superseded provenance.
