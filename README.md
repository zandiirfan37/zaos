# Zandi agent foundation (ZAOS)

`.agents` is Zandi's reusable agent intelligence — the Zandi Agentic Operating
System. It is doctrine, adapters, and skills; not a software runtime.

| Folder | Owns | Loaded |
| --- | --- | --- |
| `instructions/` | Canonical doctrine: `BIG_SOP.md` (durable spine), `ENGINEERING_DOCTRINE.md` (on-demand engineering/ML layer), `PROJECT_INTELLIGENCE_SOP.md`, `LEGACY_MIGRATION_POLICY.md`, `FRAMEWORK_IMPROVEMENT_LOOP.md`, `START_HERE_FOR_NEW_CHAT.md`. Own Git repo. | `BIG_SOP` always; rest on demand |
| `engines/` | Thin, human-authored Claude + Codex adapters that route to the doctrine. Never runtime state, never duplicated doctrine. | at engine bootstrap |
| `skills/` | Reusable on-demand expertise (`SKILL.md` + `references/`, Agent Skills shape). Added only against repeated real need; TESTED before TRUSTED. | on demand, per task |
| `library/` | Zandi-curated knowledge cards. A skill may cite one. | never automatically |
| `reference/` | Read-only *vendored external* material kept for pattern lookup (`reference/ecc/` = pinned ECC checkout; provenance `reference/ecc.lock.json`). Never installed or activated. | never automatically |
| `_retired/` | Frameworks Zandi evaluated and stood down (`ecc-zandi-profile/`, `zaine/`). Inert history; retrieval notes in `instructions/CURRENT_STATE.md`. | never |

Runtime engine state belongs in `.runtime/engines/`. Projects belong in
`projects/`. Secrets belong in `.secrets/`.

**Principles:** one owner per concept; minimum sufficient context; lazy
capability loading; no blind clones; no empty structure without a concept that
already owns it; complexity must pay rent.
