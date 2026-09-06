# Zandi skill metadata — Evidence Evaluation

- **Name:** evidence-evaluation
- **Category / status:** ASSURANCE / TESTED (fast intake)
- **Owner:** claim-to-source support and credibility assessment; it does not
  establish project, scientific, legal, or medical authority.
- **Sources:** `NousResearch/hermes-agent` grounded-citations at
  `693641aa8b4359c602283bdbbc14041e03bc47bc`; `isvlasov/rageatc-oss`
  verifying-claims pattern at `e59f63b9f12a913d6f3d76fc6d8f200a0fc93ac7`.
- **Adaptation:** retained direct-support, evidence-versus-memory, and
  claim-type distinctions; removed source-storage scripts, delegated agents,
  and domain-specific policy machinery.
- **Fast-intake checks:** `quick_validate.py`; smoke scenarios for a primary
  source, citation padding, and a non-factual opinion.
- **Verification (2026-09-07):** validator passed; a read-only Codex routing
  smoke selected `evidence-evaluation` for direct citation support.
- **Promotion:** real verification work before TRUSTED.
