# Current Zandi State

Zandi root: `/home/pc_pusaka/zandi`. Canonical workspace areas are `.agents/`,
`.runtime/`, `.secrets/`, and `projects/`. Projects and framework repositories
own their own Git history; this file is workspace state, not project state.

## Authority and routing

`BIG_SOP.md` is the single durable workspace doctrine. This file supplies only
current facts. Engine bootstraps are thin native routers: Codex at
`.runtime/engines/codex/AGENTS.md`; Claude at
`.runtime/engines/claude/CLAUDE.md`. Project-local `AGENTS.md` / `CLAUDE.md`,
`PROJECT_STATE.md`, and relevant contracts remain local authority.

## Engines and skills

`CODEX_HOME=/home/pc_pusaka/zandi/.runtime/engines/codex`.
`CLAUDE_CONFIG_DIR=/home/pc_pusaka/zandi/.runtime/engines/claude`.

The sole shared-skill root is `.agents/skills/`. Current TESTED skills:

- `ui-ux-pro-max` — DOMAIN
- `ask-the-council` — REASONING
- `ml-research` — DOMAIN

Skills, library material, ECC, and archive material load only when relevant.
ECC remains optional assurance; it is not normal bootstrap context.

## Project state

Every active project owns `<project-root>/PROJECT_STATE.md`; update it only for
meaningful state transitions. Historical evidence remains under `archive/` and
is not current operating authority.
