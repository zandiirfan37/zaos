# Engine adapters

The Git-tracked ZAOS adapters are
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

## Human launcher and session capability

Primary human usage is the native commands themselves:

```
cd <project-or-workspace>
codex
claude
```

Run `bin/zaos-install-native-shims install` once (user-local, reversible) to
put scoped shims for `codex`/`claude` on `PATH` ahead of the vendor binaries.
Inside this ZAOS-managed workspace (the parent of `.agents`), the shims
transparently route through `bin/zaos`: project discovery, task-class
capability selection, and the internal engine adapter, exactly as before.
Outside the workspace, a shimmed `codex`/`claude` is byte-for-byte the vendor
binary — no ZAOS involvement, no behavior change. The real binaries are
preserved at `~/.local/lib/zaos-real-bin/` and stay directly reachable at all
times as an escape hatch (also: `ZAOS_INTERNAL_EXEC=1 codex ...` bypasses
routing without touching PATH). `bin/zaos-install-native-shims uninstall`
restores the original entries. See
[`SESSION_PROVISIONING.md`](SESSION_PROVISIONING.md) for the recursion-guard
and capability-declaration mechanics.

`bin/zaos` (with public engine names `codex` / `claude`; `terra` is a legacy
admin alias) and `bin/zaos-session`
remain the explicit admin/debug interfaces — use them directly for
`--print-plan`, an explicit project path, or when diagnosing a broken shim.
At the non-Git workspace root, routing intentionally enters `.agents`
framework maintenance rather than exposing a Git error.

Capability selection is task-class-driven, not flag-driven: `.agents` always
gets `ZAOS_MAINTENANCE`; a project opts into `FULL_LOCAL_DEV` by declaring it
in its own `.zaos-capability` file (no project-name hardcoding); everything
else gets the normal mutative profile. `zaos ... --local-dev` remains an
explicit manual override for the admin path.

## Resource policy

| Engine | Normal model | Normal effort |
| --- | --- | --- |
| Codex | GPT-5.6 Terra | medium |
| Claude | Sonnet | medium |

Use high effort only for consequential architecture, difficult debugging,
scientific ambiguity, security/release assurance, or an explicit
Human/Orchestrator request. Model and engine policy belongs here, not in
`BIG_SOP.md`.
