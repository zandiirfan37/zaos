# Zandi agent foundation

`.agents` is Zandi's reusable agent intelligence.

- `instructions/` — global operating doctrine and current workspace guidance.
- `frameworks/` — external harnesses and frameworks, including ECC and ZAINE.
- `skills/` — reusable on-demand expertise, added only as it becomes useful.
- `library/` — curated references and knowledge; never automatically loaded.
- `engines/` — human-authored engine-specific adapters only, never runtime state.

Runtime engine state belongs in `.runtime/engines/`. Projects belong in
`projects/`. Secrets belong in `.secrets/`.

**Principles:** one owner per concept; minimum sufficient context; no blind
clones; no empty structure without purpose.
