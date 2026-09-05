# Current Zandi State

Zandi is rooted at `/home/pc_pusaka/zandi`; the root is intentionally
behaviorally non-Git. Frameworks and projects are independent Git repositories
with their own history, status, and remote policy. This file covers the
workspace and frameworks, not per-project state.

## Frameworks

| Framework | Path | Status |
| --- | --- | --- |
| ECC-Zandi Standard-Advanced | `.agents/frameworks/ecc/zandi-profile` | **active** — the validated project-workflow adapter for selected ECC guidance; route playbooks in `prompts/`; component lock in `COMPONENTS.lock.json`. Profile changes are local commits needing explicit approval and do not touch ECC upstream. |
| ECC upstream | `.agents/frameworks/ecc/upstream` @ `005eff40fd4a4ac005da7a70e713459175385516` | read-only sparse reference; keep clean and updateable; no install or activation. |
| ZAINE | `.agents/frameworks/zaine` | frozen. Inspect its own instructions and status before any use. |

The adapter is not an ECC installation or global integration. Use the smallest
framework guidance that fits; do not force a framework the project does not
need.

## Agents and routing

Two peer implementation/review agents — Codex CLI (primary implementer when
available) and Claude Code CLI (backup / takeover implementer, independent
reviewer). ChatGPT is the Orchestrator; the Human Lead is final authority. One
active writer per working tree. Full roles, model routing, handoff,
concurrency, and the Claude operating budget are in `MULTI_AGENT_ROUTING.md`.

Agent config lives in `/home/pc_pusaka/zandi/.runtime/engines/codex`
(`CODEX_HOME`, migrated from the former `/home/pc_pusaka/zandi/.codex`) and,
pending final cutover, `/home/pc_pusaka/zandi/.claude`; `~/.claude` is
currently a compatibility symlink to `/home/pc_pusaka/zandi/.claude`. A
prepared copy already exists at
`/home/pc_pusaka/zandi/.runtime/engines/claude` (`CLAUDE_CONFIG_DIR`,
exported for future shells) but the live symlink is intentionally left in
place until a session that is not itself the active writer can finalize the
cutover. `~/.codex/packages/` remains the Codex installer/updater's own
binary store — separate from `CODEX_HOME` and not relocated. Global
configuration mutation, including `~/.codex` and `~/.claude` contents,
remains an explicit approval boundary.

## Project state protocol

Every active project maintains one canonical
`<project-root>/PROJECT_STATE.md` (template:
`templates/PROJECT_STATE.template.md`) describing where that project is now.
Keeping it current is part of the Definition of Done for any state-changing
sprint; see `ZANDI_MASTER_WORKFLOW.md`.

## Validated evidence

`projects/ecc-minilab-pilot` is the validated ECC-Zandi pilot. Read
`VALIDATION_LEDGER.md` before treating any pilot lesson as reusable guidance.
