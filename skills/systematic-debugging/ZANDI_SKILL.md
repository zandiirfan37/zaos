# Zandi skill metadata — Systematic Debugging

- **Name:** systematic-debugging
- **Category / status:** WORKFLOW / TESTED (fast intake)
- **Owner:** Zandi adaptation; root-cause decision only.
- **Source:** `obra/superpowers` `systematic-debugging`, inspected at `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` (2026-09-07).
- **Adaptation:** retained reproduce → trace/compare → hypothesis → verify; removed universal mandates, subagent assumptions, and framework coupling.
- **Overlap:** no existing Zandi skill owns root-cause diagnosis. Engineering doctrine owns assurance and project authority.
- **Fast-intake checks:** `quick_validate.py`; three routing smoke scenarios (test failure, production symptom, known one-line typo) reviewed against scope.
- **Promotion:** real-project use before TRUSTED.
