# Current Zandi State

Zandi root: `/home/pc_pusaka/zandi`. Active workspace areas are `.agents/`,
`.runtime/`, `.secrets/`, and `projects/`. Inert history lives in `.archive/`.
Projects and vendored repositories own their own Git history; this file is
workspace state, not project state.

## Authority and routing

`BIG_SOP.md` is the single durable workspace doctrine. `ENGINEERING_DOCTRINE.md`
is its on-demand deeper layer for engineering/data/ML work (subordinate, never a
second authority). `PROJECT_INTELLIGENCE_SOP.md` is the on-demand prior-art /
project-refoundation track. `MAINTENANCE_AND_MIGRATION.md` covers how doctrine
evolves from evidence and how legacy material is migrated or retired. This file
supplies only current facts.

Engine bootstraps are thin native routers: Codex at
`.runtime/engines/codex/AGENTS.md`; Claude at `.runtime/engines/claude/CLAUDE.md`.
Canonical adapters are `.agents/engines/{codex/AGENTS.md, claude/CLAUDE.md}` —
route only, never duplicate doctrine. The Codex runtime copy must be refreshed
from the canonical adapter whenever that adapter changes (Codex has no proven
native import). Project-local `AGENTS.md` / `CLAUDE.md`, `PROJECT_STATE.md`, and
relevant contracts remain local authority.

`CODEX_HOME=/home/pc_pusaka/zandi/.runtime/engines/codex`.
`CLAUDE_CONFIG_DIR=/home/pc_pusaka/zandi/.runtime/engines/claude`.

Responsive Preflight is prior-art-first for nontrivial new builds, major
rebuilds, and re-foundations: when external references or data could change the
direction, route through Project Intelligence / project-refoundation before
material greenfield implementation. This is proportional, not a universal gate.

## Active .agents/ components

| Area | Status | Owner / notes |
| --- | --- | --- |
| `.agents/instructions/` | LIVE | Canonical doctrine. `README` + `BIG_SOP` + `ENGINEERING_DOCTRINE` + `PROJECT_INTELLIGENCE_SOP` + `MAINTENANCE_AND_MIGRATION` + this file, plus `archive/` (historical evidence, not authority) and `templates/`. Own Git repo (see "Repository layout"). |
| `.agents/engines/` | LIVE | Thin Claude + Codex adapters (route only) + `bin/zaos-session` launcher + `tools/`. |
| `.agents/engines/tools/zaos-doctor` | LIVE | Read-only, advisory control-plane diagnostic (git / runtime-contract reconcile / stale-job / resource / leak-safe secret / clock skew / workbench→production promotion guard / capability hint). Engine-neutral, invoked by path. **Advisory only** — not a lifecycle authority, not a gate, not permission to mutate, not canonical project truth; exit code is information, never a block; defines no new hard-block class. Promoted from `projects/06_zaos_control_plane/tools/` 2026-09-10 after Pilots #1–#4. Self-contained regression suite: `tools/tests/run_tests.sh`. Rollback anchor: tag `zaos-pre-doctor-promotion-20260910`. Known gap: JOB stall/orphan heuristic has fixture coverage only — real long-running-job field exercise still owed. `zaos-handoff` and `ORCHESTRATOR_PRIMER` were **not** promoted (remain project-06 prototypes). |
| `.agents/skills/` | LIVE | Sole shared-skill root. On-demand, lazy, task-matched. Add a skill as `.agents/skills/<skill>/SKILL.md` (+ `references/`); no runtime-framework change and no standing-context growth. TESTED: `ui-ux-pro-max`, `ask-the-council`, `ml-research`, `browser-qa`, plus engineering/project and general intellectual/creative fast-intake skills. PATCH: `lit-review`. DRAFT: `project-refoundation`, `project-architecture`, `medical-imaging-research`. |
| `.agents/eval/` | LIVE | ZAOS-native evaluation harness (`zaos_eval.py`, stdlib). On-demand only; drives the `claude`/`codex` CLIs. Evidence → `.runtime/eval/` (disposable). |
| `.agents/library/` | LIVE (passive) | Zandi-curated knowledge cards. Never auto-loaded; a skill may cite one. |
| MCP / hooks / plugins | NONE | Zero configured in either engine, by decision. |

`.agents/_retired/` and `.agents/reference/` no longer exist in the active tree
(retired 2026-09-08 — see `.archive/`).

## Archive

`/home/pc_pusaka/zandi/.archive/` is retrieval/provenance storage, never active
authority. Nothing in `.agents/`, `.runtime/`, or `projects/` depends on an
`.archive/` path.

| Path | Contents |
| --- | --- |
| `.archive/01_legacy_systems/zaine/` | ZAINE engineering platform. Evaluated, never adopted (no project used its artifact/extension contracts). Inert; inner Git history intact. Retrieval notes in `MAINTENANCE_AND_MIGRATION.md`. |
| `.archive/01_legacy_systems/ecc-zandi-profile/` | "ECC-Zandi Standard-Advanced" profile. Its engineering doctrine was promoted to `ENGINEERING_DOCTRINE.md` (the web-app quality guardrail and depth-by-scale ladder folded in 2026-09-08). |
| `.archive/01_legacy_systems/ecc-reference/` | Pinned sparse checkout of `affaan-m/ECC` @ `005eff40` (its `.git` + `ecc.lock.json` preserved). Never installed or activated. |
| `.archive/02_closed_pilots/zaine-taskboard-pilot/` | Closed taskboard validation pilot. |
| `.archive/02_closed_pilots/ecc-minilab-pilot/` | Closed ECC-Zandi MiniLab validation pilot. |
| `.archive/03_project_history/gradtime/` | Predecessor of the active `01_gradtime_v2` project, plus its loose migration reports under `migration_reports/`. Inner Git history intact (branch `gen2-research`). |
| `.archive/04_legacy_runtime/` | Shadowed pre-cutover Claude engine/config backup. |
| `.archive/05_personal_archives/` | Personal ZIP archives moved out of the active tree. |

## Repository layout

Zandi-owned agent-infra is two Git repos: `.agents/` (README, `engines/`,
`skills/`, `eval/`, `library/`) and the nested `.agents/instructions/` (doctrine).
Kept separate for now because merging risks the doctrine history; consolidating
`instructions/` into `.agents/` via `git subtree` is **deferred debt**, not
active scope. Archived items keep their own inner Git histories.

## Runtime roots

`.runtime/` is derived, disposable, not Git-tracked. `.runtime/uv/` (centralized
uv Python, tools, cache), `.runtime/bin/` (uv-managed CLIs), and
`.runtime/browsers/playwright/` (chromium build 1234 + ffmpeg, ~656 MB) are
cleaned only by their own tool-native commands, never automatically. The
Playwright payload is owned by the `browser-qa` skill and is regenerable.

## Root vendor/tool artifacts

`.codex/` (empty), `.claude/` (Claude Code project-scope: `scheduled_tasks.lock`),
and the `.git/` stub (Claude Code runtime marker holding `info/exclude`) are
fixed tool conventions at the workspace root. They are covered by the root
`.gitignore` and are not fought for cosmetic cleanliness; the `.git/` stub is not
removed.

## Project state

Active projects, canonical numbered map (append-only; a closed project keeps its
retired number):

| Path | Project |
| --- | --- |
| `projects/01_gradtime_v2/` | Graduation-time prediction, active successor to the archived `gradtime`. |
| `projects/02_paper-q1-vis-tp/` | Q1 paper — VIS-TP medical-imaging research. |
| `projects/03_smart_attendance/` | Smart attendance system. |
| `projects/04_zaos/` | Literary-philosophical book project narrated by "ZAOS". |

Next new project: `05_<name>`.

Every active project owns `<project-root>/PROJECT_STATE.md`; update it only for
meaningful state transitions. Each project standard: 3–7 root docs, an
`00_workbench/` pre-production laboratory (fixed `00_` prefix; may hold
sequentially numbered subprojects; absorbs simulation/research/prototype/evidence
work rather than a parallel top-level zone), semantic `src/`, `tests/`, and
numbered human-sequence stages where useful. Canonical production/research areas
must not depend on `00_workbench/` paths, and production stays free of scratch or
aborted-iteration files. Promotion is a clean rewrite into a canonical location,
not a folder move. Templates: `instructions/templates/`.

`01_gradtime_v2` still uses `workbench/` (not `00_workbench/`): its production
app and ops code read evidence through hash-locked `contracts/*.json` and
`releases/model/` artifacts that embed `workbench/` paths, so a rename collides
with the LOCK-3 scientific integrity tests. Normalisation is deferred to a
Human-Lead-approved promotion sprint that re-homes the production-read evidence
and re-locks, not a mechanical rename.

Historical evidence under `instructions/archive/` (including `VALIDATION_LEDGER.md`)
is not current operating authority.
