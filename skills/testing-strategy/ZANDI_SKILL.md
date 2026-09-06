# Zandi skill metadata — Testing Strategy

- **Name:** testing-strategy
- **Category / status:** ASSURANCE / TESTED (fast intake)
- **Owner:** selecting proportionate evidence for a changed implementation
  claim; project test contracts and code review remain separate owners.
- **Sources:** native extraction from BIG_SOP verification levels and OpenAI
  official model guidance on meaningful, proportional testing (accessed
  2026-09-07); no external runtime dependency.
- **Adaptation:** makes claim-to-check selection reusable without imposing
  TDD, a full suite, or a fixed test framework.
- **Fast-intake checks:** `quick_validate.py`; smoke scenarios for a pure
  helper, a route integration, and a green-but-irrelevant suite.
- **Promotion:** real-project use before TRUSTED.
