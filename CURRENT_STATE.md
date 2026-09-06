# Current Zandi State

Zandi root: `/home/pc_pusaka/zandi`. Canonical workspace areas are `.agents/`,
`.runtime/`, `.secrets/`, and `projects/`. Projects and vendored repositories
own their own Git history; this file is workspace state, not project state.

## Authority and routing

`BIG_SOP.md` is the single durable workspace doctrine. `ENGINEERING_DOCTRINE.md`
is its on-demand deeper layer for engineering/data/ML work (subordinate, never a
second authority). This file supplies only current facts. Engine bootstraps are
thin native routers: Codex at `.runtime/engines/codex/AGENTS.md`; Claude at
`.runtime/engines/claude/CLAUDE.md`. Project-local `AGENTS.md` / `CLAUDE.md`,
`PROJECT_STATE.md`, and relevant contracts remain local authority.

`CODEX_HOME=/home/pc_pusaka/zandi/.runtime/engines/codex`.
`CLAUDE_CONFIG_DIR=/home/pc_pusaka/zandi/.runtime/engines/claude`.

## Component status

| Area | Status | Owner / notes |
| --- | --- | --- |
| `.agents/instructions/` | LIVE | Canonical doctrine. `BIG_SOP` + `ENGINEERING_DOCTRINE` + `PROJECT_INTELLIGENCE_SOP` + `LEGACY_MIGRATION_POLICY` + `FRAMEWORK_IMPROVEMENT_LOOP` + `START_HERE`. Own Git repo (see "Repository layout"). |
| `.agents/engines/` | LIVE | Thin Claude + Codex adapters. Route only; never duplicate doctrine. |
| `.agents/skills/` | LIVE | Sole shared-skill root. On-demand only. TESTED: `ui-ux-pro-max` (DOMAIN), `ask-the-council` (REASONING), `ml-research` (DOMAIN), `browser-qa` (WORKFLOW), plus fast-intake procedural capabilities: `systematic-debugging`, `scope-discipline`, `code-review`, `requirements-framing`, `implementation-planning`, `testing-strategy`, `technical-documentation`, `frontend-performance`, and `scientific-writing`. PATCH: `lit-review` (real pilot blocked by available synthesizer auth; not trusted). DRAFT: `project-refoundation`, `project-architecture`, `medical-imaging-research`. Skill files follow the Agent Skills shape (`SKILL.md` + `references/`); `ZANDI_SKILL.md` records provenance. |
| `.agents/eval/` | LIVE | ZAOS-native evaluation harness (`zaos_eval.py`, stdlib). On-demand only; drives the `claude`/`codex` CLIs. Evidence → `.runtime/eval/` (disposable). |
| `.agents/library/` | LIVE (passive) | Zandi-curated knowledge cards. Never auto-loaded; a skill may cite one. |
| `.agents/reference/` | REFERENCE | Read-only vendored external material for pattern lookup. `reference/ecc/` = pinned sparse checkout of `affaan-m/ECC` @ `005eff40` (provenance: `reference/ecc.lock.json`). Never installed, activated, or default-loaded. |
| `.agents/_retired/ecc-zandi-profile/` | RETIRED | Was the "ECC-Zandi Standard-Advanced" profile. Retired 2026-09-06: its engineering doctrine was promoted verbatim to `instructions/ENGINEERING_DOCTRINE.md`; its container had drifted (dangling refs to deleted `ZANDI_MASTER_WORKFLOW.md`). The web-app quality guardrail and depth-by-scale ladder remain in `_retired/ecc-zandi-profile/AGENTS.ecc-standard-advanced.md` pending a reviewed fold into `ENGINEERING_DOCTRINE.md`. |
| `.agents/_retired/zaine/` | RETIRED | "ZAINE" engineering platform. Retired 2026-09-06: effectively never used in day-to-day work; its validators validate a `ZAINE Artifact Contract v1` / `.zaine/extensions/inventory.toml` format that no project adopted. Not deleted — inert, full history intact. If ZAOS later adds live extensions (MCP / hooks / plugins), start the capability-manifest + drift model from `_retired/zaine/scripts/extension_governance.py` and `_retired/zaine/specs/ZAINE_EXTENSION_GOVERNANCE_v1.md`; the artifact/research contract validators and `project_doctor.py` are there too. Promote only against a real consumer, never speculatively. |
| MCP / hooks / plugins | NONE | Zero configured in either engine, by decision. |

## Repository layout

Zandi-owned agent-infra is two Git repos: `.agents/` (README, `engines/`,
`skills/`, `library/`) and the nested `.agents/instructions/` (doctrine). They
are kept separate for now because merging them risks the doctrine history;
`reference/ecc/` is a third repo but vendored (own upstream remote). `_retired/*`
keep their own inert Git histories. Consolidating `instructions/` into `.agents/`
via `git subtree` is open debt, not urgent now that the ECC-Zandi profile (the
prior drift victim) is retired.

## Runtime roots

`.runtime/` is derived, disposable, not Git-tracked. `.runtime/uv/` (centralized
uv Python, tools, cache), `.runtime/bin/` (uv-managed CLIs), and
`.runtime/browsers/playwright/` (chromium build 1234 + ffmpeg, ~656 MB) are
cleaned only by their own tool-native commands, never automatically.

The Playwright payload is owned by the `browser-qa` skill (chromium build 1234,
matched to `playwright==1.62.0` which `uv run` resolves on demand — no `node`,
nothing downloaded). Regenerable if deleted.

## Project state

Every active project owns `<project-root>/PROJECT_STATE.md`; update it only for
meaningful state transitions. Active projects: `gradtime`, `gradtime_v2`,
`paper-q1-vis-tp`, plus the closed pilots `zaine-taskboard-pilot` and
`ecc-minilab-pilot`. Historical evidence under `instructions/archive/` (including
`VALIDATION_LEDGER.md`, which predates the `BIG_SOP` consolidation) is not
current operating authority.
