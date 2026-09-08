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

## Adaptive zones

Put evolvable planning and design in `00_workbench/`: a master plan, chapter or
continuity map, experimental outline, alternative argument structure, temporary
research plan, probes, reviews, and unresolved specifications belong there
first. A research/writing project may converge to this shape; use only the
zones it has earned:

```text
00_workbench/
  01_design/
  02_outline_experiments/
  03_review_notes/
01_research/
02_evidence/
03_manuscript/
04_deliverables/
```

The numbered top-level paths express human workflow order, not a mandatory
checklist. Analysis code and tools remain semantic where needed:
`src/<pkg>/`, `tests/`, `data/`, `config/`, and manifests should not be numbered
when imports, discovery, or tooling expect those names. Do not scaffold empty
folders or permanent documents merely because this example contains them.

## Promotion

When a planning or research decision becomes durable project truth, understand
the winner and promote a clean distilled version into its canonical zone →
verify proportionally → update `PROJECT_STATE.md` and evidence/contracts as
needed. Workbench artifacts can remain as provenance, but canonical
research/evidence and deliverables must not depend on them or cite them as
authoritative results.
