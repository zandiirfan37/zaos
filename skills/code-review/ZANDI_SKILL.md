# Zandi skill metadata — Code Review

- **Name:** code-review
- **Category / status:** ASSURANCE / TESTED (fast intake)
- **Owner:** diff-based implementation-risk review; tests and project authority remain separate owners.
- **Sources:** `garrytan/gstack` review/plan-to-QA pattern at `0530392821c277b95e5cd65aa9d9fda4248718b2`; `obra/superpowers` requesting-code-review at `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`.
- **Adaptation:** removed mandatory subagents, PR/merge workflow, and engine-specific dispatch assumptions; retained actual-diff, requirements, and verification review.
- **Fast-intake checks:** `quick_validate.py`; smoke scenarios for a risky refactor, small text edit, and test-only green-but-wrong claim.
- **Promotion:** real-project use before TRUSTED.
