# Engine adapters

The Git-tracked, Zandi-authored adapters are
[`codex/AGENTS.md`](codex/AGENTS.md) and
[`claude/CLAUDE.md`](claude/CLAUDE.md). They route rather than duplicate the
one canonical doctrine: [`../instructions/BIG_SOP.md`](../instructions/BIG_SOP.md).
`CURRENT_STATE.md` is conditional, not bootstrap payload.

## Routing model

`ENGINE BOOTSTRAP → minimal engine adapter → BIG_SOP + responsive preflight when substantive →
CURRENT_STATE when relevant → project-local authority/state/contracts →
relevant skill only → current task`

Default exclusions are unrelated skills, Council, `.archive/` material (retired
frameworks, vendored checkouts, closed pilots, project history), deep library
material, and unrelated project history.

## Deployment

Claude's runtime bootstrap is a native import stub for the canonical Claude
adapter. Codex has no proven equivalent native import; deploy the canonical
Codex adapter as an exact runtime copy at
`.runtime/engines/codex/AGENTS.md` when runtime state is created or refreshed.
Runtime state is disposable and is not Git-tracked.

Shared skills have one physical owner at `.agents/skills/<skill>/SKILL.md`.
Claude's normal launches use canonical-path, task-matched lazy routing; do not
copy or symlink skills into either engine tree. `--plugin-dir` is an optional
future per-session capability, not the default architecture.

## Session capability

Use [`bin/zaos-session`](bin/zaos-session) to select capability before a new
engine session. Its three small modes and the exact Codex/Claude invocation
routes are documented in [`SESSION_PROVISIONING.md`](SESSION_PROVISIONING.md).

## Resource policy

| Engine | Normal model | Normal effort |
| --- | --- | --- |
| Codex | GPT-5.6 Terra | medium |
| Claude | Sonnet | medium |

Use high effort only for consequential architecture, difficult debugging,
scientific ambiguity, security/release assurance, or an explicit
Human/Orchestrator request. Model and engine policy belongs here, not in
`BIG_SOP.md`.
