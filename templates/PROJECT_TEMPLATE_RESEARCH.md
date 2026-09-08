# Project template — research / paper project

Minimal adaptable standard. Create only what the project needs; never scaffold
empty directories. Number human sequence; keep machine/semantic names stable.

## Root documents (3–7)

- `README.md` — what / why / how to reproduce. **Required.**
- `PROJECT_STATE.md` — single compact current-state artifact. **Required.**
- `PROJECT_DIRECTION.md` — where useful (scope, claim boundary, stage plan).
- `AGENTS.md` — only when local rules genuinely diverge from `BIG_SOP.md`.
- machine manifests (`pyproject.toml`, `uv.lock`, `.gitignore`) if analysis code
  exists — not counted as documentation.

## Zones

| Path | Purpose | Notes |
| --- | --- | --- |
| `00_workbench/` | unrestricted exploration: probes, dead ends, alternative specs, audits, migration attempts, temporary evidence | canonical research must not depend on it |
| `research/` | canonical converged findings, in numbered stages | `research/01_<stage>/`, `research/02_<stage>/`, … plus `literature/` |
| `src/<pkg>/`, `tests/` | analysis code | only if analysis code exists; `src/` semantic, never numbered |
| `data/` | inputs | usually gitignored, lineage tracked |
| `evidence/` | verification artifacts cited by `PROJECT_STATE.md` | only when needed |
| `deliverables/` | manuscript, `figures/`, `tables/`, submission package | |

## Promotion

Understand the winning analysis → re-run/rewrite it clean into `research/NN_*` →
verify proportionally → update `PROJECT_STATE.md`. Workbench probes stay as
superseded provenance; they are never cited as canonical results.
