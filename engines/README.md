# Engine adapters

The one canonical workspace doctrine is
[`../instructions/BIG_SOP.md`](../instructions/BIG_SOP.md). Its compact current
facts are in `../instructions/CURRENT_STATE.md`; neither is copied here.

Codex uses the thin native bootstrap at
`.runtime/engines/codex/AGENTS.md`. Claude uses the thin native bootstrap at
`.runtime/engines/claude/CLAUDE.md`. Each contains paths and routing only:
canonical doctrine, conditional current state, local project authority, and the
shared skill root.

Codex and Claude execution/session/cache state remains in `.runtime/engines/`.
Shared skills have one physical owner at `.agents/skills/<skill>/SKILL.md`.
Codex discovers that root natively. Claude's installed client does not register
an external skill root; its bootstrap directs task-matched loading from the
same canonical paths. Do not copy or symlink skills into either engine home.

Archive material, library references, and ECC are explicit on-demand context;
they are not bootstrap payload.
