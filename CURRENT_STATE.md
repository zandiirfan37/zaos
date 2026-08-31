# Current Zandi State

Zandi is rooted at `/home/pc_pusaka/zandi`. Its root remains intentionally
behaviorally non-Git; frameworks and projects are independent Git repositories
with their own history, status, and remote policy.

## Framework state

- ZAINE: `/home/pc_pusaka/zandi/frameworks/zaine` — frozen for now.
- ECC upstream: `/home/pc_pusaka/zandi/frameworks/ecc/upstream` at
  `005eff40fd4a4ac005da7a70e713459175385516` — keep clean and updateable.
- ECC-Zandi Standard-Advanced:
  `/home/pc_pusaka/zandi/frameworks/ecc/zandi-profile` — the validated,
  controlled project-workflow adapter for selected ECC reference material.

The adapter is not an ECC installation or global integration. Global
configuration mutation, including `~/.codex` and `~/.claude`, remains forbidden
unless explicitly approved.

## Validated project evidence

`/home/pc_pusaka/zandi/projects/ecc-minilab-pilot` is the validated ECC-Zandi
pilot. Read `VALIDATION_LEDGER.md` before treating its lessons as reusable
guidance.

## Model routing

- Terra Medium: implementation and bounded local changes.
- Terra High: independent audit and review.
- XHigh: exceptional complex design or debugging only.
