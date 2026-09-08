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

## Adaptive zones

Start with `00_workbench/` for evolvable design, planning, experiments, audits,
scratch, temporary evidence, and alternatives. A code/AI project might then
need only the following shape; select and rename zones for the actual project:

```text
00_workbench/
  01_design/
  02_experiments/
  03_audits/
01_research/
02_data_pipeline/
03_evaluation/
src/<pkg>/
tests/
contracts/
config/
runtime/
```

After `00_workbench/`, number human-facing top-level workflow zones in their
intended order. Do not create every illustrated zone or any empty scaffold.
Keep machine- and tool-sensitive names unnumbered: `src/`, `tests/`, `config/`,
`contracts/`, `runtime/`, `migrations/`, `scripts/`, framework directories, and
manifests retain their semantic names. `pipeline/`, `data/`, `evidence/`, and
`deliverables/` are optional when the project needs them.

## Promotion

Understand the winning experiment or design → rewrite/refactor it clean into the
canonical area → verify proportionally → update `PROJECT_STATE.md` and contracts
as needed. Do not move messy workbench artifacts verbatim into production;
production must not depend on `00_workbench/`, while the original may stay as
superseded provenance.
