# ZAOS current state

This is compact framework state, not a catalogue of a maintainer’s private
workspace. The canonical framework is one Git repository rooted at the ZAOS
checkout. `instructions/` is an ordinary tracked directory whose prior
standalone history was merged in commit `a870c4e`.

## Current architecture

- Native `codex` and `claude` are the normal human entry points inside the
  configured workspace; `zaos` is an admin/debug command.
- Scoped user-local shims fail open to preserved raw vendor commands outside a
  configured workspace or if ZAOS is unhealthy.
- Project capability comes from `.zaos-capability`; normal projects do not
  receive `FULL_LOCAL_DEV` merely because an engine starts.
- Runtime engine configuration is user-local and disposable. Framework files,
  projects, secrets, and generated runtime state have separate ownership.
- `zaos doctor`, `zaos engines status`, `zaos engines refresh`, and `zaos
  update` provide diagnostics, vendor-pointer maintenance, and guarded update.
- `ZAOS_EXTERNAL_PUBLISH` is an explicit admin capability for authorized
  publication tasks only; it adds outbound network access without making
  ordinary maintenance network-enabled.

## Authority

`BIG_SOP.md` is the durable doctrine. `ENGINEERING_DOCTRINE.md`,
`PROJECT_INTELLIGENCE_SOP.md`, and `MAINTENANCE_AND_MIGRATION.md` are
on-demand supporting doctrine. The two primary handoff files are
`../ZAOS_HUMAN.md` and `../ZAOS_ORCHESTRATOR.md`. Project-local instructions,
state, and contracts govern project work.

The ZAOS book/project is not part of framework packaging. Archived material is
retrieval-only and never an active dependency.
