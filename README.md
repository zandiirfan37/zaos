# Zandi agent foundation (ZAOS)

`.agents` is Zandi's reusable agent intelligence — the Zandi Agentic Operating
System. It is doctrine, adapters, and skills; not a software runtime.

| Folder | Owns | Loaded |
| --- | --- | --- |
| `instructions/` | Canonical doctrine: `README.md` (start here), `BIG_SOP.md` (durable spine), `ENGINEERING_DOCTRINE.md` (on-demand engineering/ML layer), `PROJECT_INTELLIGENCE_SOP.md`, `MAINTENANCE_AND_MIGRATION.md`, `CURRENT_STATE.md`. Own Git repo. | `BIG_SOP` always; rest on demand |
| `engines/` | Thin, human-authored Claude + Codex adapters that route to the doctrine. Never runtime state, never duplicated doctrine. | at engine bootstrap |
| `skills/` | Reusable on-demand expertise (`SKILL.md` + `references/`, Agent Skills shape). Added only against repeated real need; TESTED before TRUSTED. | on demand, per task |
| `eval/` | ZAOS-native evaluation harness (stdlib). Drives the `claude`/`codex` CLIs; evidence to `.runtime/eval/`. | on demand |
| `library/` | Zandi-curated knowledge cards. A skill may cite one. | never automatically |

Retired frameworks and vendored external checkouts live inert under
`/home/pc_pusaka/zandi/.archive/` (see `instructions/MAINTENANCE_AND_MIGRATION.md`).
Runtime engine state belongs in `.runtime/engines/`. Projects belong in
`projects/`. Secrets belong in `.secrets/`.

**Principles:** one owner per concept; minimum sufficient context; lazy
capability loading; no blind clones; no empty structure without a concept that
already owns it; complexity must pay rent.

## Human launcher

Install the tracked human-facing launcher into the user-local PATH with:

```bash
ln -sfn /path/to/zandi/.agents/engines/bin/zaos ~/.local/bin/zaos
```

Then use `zaos`, `zaos terra`, or `zaos claude` from a project worktree. See
[`engines/SESSION_PROVISIONING.md`](engines/SESSION_PROVISIONING.md) for the
small public syntax and capability behavior.
