# Zandi skill metadata — Implementation Planning

- **Name:** implementation-planning
- **Category / status:** WORKFLOW / TESTED (fast intake)
- **Owner:** short execution sequencing for an accepted multi-step change;
  requirements and project architecture remain separate owners.
- **Sources:** `obra/superpowers` writing-plans at
  `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`.
- **Adaptation:** retained dependency-first, boundary-aware, independently
  verifiable tasks; removed fixed output directories, bite-sized ceremony,
  mandatory TDD, worktrees, subagents, and handoff gates.
- **Fast-intake checks:** `quick_validate.py`; smoke scenarios for a small
  feature, a dependent migration-shaped change, and a one-file routine edit.
- **Promotion:** real-project use before TRUSTED.
