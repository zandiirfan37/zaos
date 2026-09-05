# Current Zandi State

Zandi is rooted at `/home/pc_pusaka/zandi`. The root is behaviorally non-Git; frameworks and projects own their own repositories, history, and remote policy. This file covers workspace state, not project state.

## Frameworks

| Framework | Path | Status |
| --- | --- | --- |
| ECC-Zandi adapter | `.agents/frameworks/ecc/zandi-profile` | Zandi-owned optional assurance adapter; changes require explicit approval. |
| ECC upstream | `.agents/frameworks/ecc/upstream` @ `005eff40fd4a4ac005da7a70e713459175385516` | read-only reference; no default activation. |
| ZAINE | `.agents/frameworks/zaine` | frozen; inspect its own guidance before use. |

## Agents and runtime

ChatGPT orchestrates; Codex and Claude are peer executors/reviewers. One active writer per working tree. The durable operating rules are in `BIG_SOP.md`.

Execution state lives in `.runtime/engines/codex` (`CODEX_HOME`) and `.runtime/engines/claude` (`CLAUDE_CONFIG_DIR`). Do not modify engine state or global configuration unless explicitly authorized.

## Project state

Every active project owns one current `<project-root>/PROJECT_STATE.md`. Update it only for meaningful state transitions; it is not a task log. The template is `templates/PROJECT_STATE.template.md`. See `BIG_SOP.md` for the normal loop.

## Historical evidence

`archive/VALIDATION_LEDGER.md` records prior pilot evidence. It is historical, not current operating authority.
