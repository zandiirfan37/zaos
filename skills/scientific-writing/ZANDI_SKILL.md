# Zandi skill metadata — Scientific Writing

- **Name:** scientific-writing
- **Category / status:** WORKFLOW / TESTED (fast intake)
- **Owner:** evidence-bounded expression of a scientific manuscript claim;
  project-local scientific method, results, and citations remain authority.
- **Sources:** native adaptation of the Paper_Q1 lit-review evidence boundary
  and `anthropics/skills` document-coauthoring structure at
  `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`.
- **Adaptation:** retained claim/evidence/limitation coherence; removed generic
  authoring stages and explicitly forbids using writing as scientific
  validation or claim promotion.
- **Fast-intake checks:** `quick_validate.py`; smoke scenarios for a results
  paragraph, an over-generalized conclusion, and a citation not in the local
  evidence.
- **Promotion:** real-project use before TRUSTED.
