# Zandi skill metadata — Web Research

- **Name:** web-research
- **Category / status:** WORKFLOW / TESTED (fast intake)
- **Owner:** proportionate discovery and source-grounded answering over current
  external material; `lit-review` remains the owner of curated local paper
  corpora.
- **Sources:** `anthropics/knowledge-work-plugins` customer-research at
  `1f517b9de47e827c80cd933ed364e16838072239`; `ysm-dev/skills` web-search
  research trigger pattern at `4455e4e797dd0e820fd016a875585f245becf8dd`.
- **Adaptation:** removed customer/CRM assumptions, automatic knowledge-base
  writes, and fixed reports; retained freshness detection, source attribution,
  confidence, and uncertainty.
- **Fast-intake checks:** `quick_validate.py`; routing smoke for a stable
  question, a current fact, and a multi-source disputed topic.
- **Verification (2026-09-07):** validator passed; a read-only Codex routing
  smoke selected `web-research` for a current contested fact.
- **Promotion:** real-project or real intellectual-work use before TRUSTED.
