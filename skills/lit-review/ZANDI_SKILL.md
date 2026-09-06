# Zandi skill metadata — lit-review

- **Name:** lit-review
- **Category:** WORKFLOW (tool wrapper)
- **Owner:** Zandi (native)
- **Status:** PATCH / NOT YET TRUSTED — the Paper_Q1 real-corpus pilot validated
  corpus/retrieval mechanics but could not complete grounded synthesis with the
  available authenticated engines; see the project evidence before promotion.
- **Created:** 2026-09-06 (capability-expansion wave 2, Track A)
- **Capability:** citation-grounded Q&A over a curated local corpus of papers/notes.
- **Why native, not PaperQA2:** PaperQA2 requires an LLM endpoint via litellm — a
  cloud API key + budget, or a local Ollama stack (~3 GB models, CPU-slow, no GPU
  here). Both are Human Lead decisions. `litqa.py` gets ~80% of the value
  (retrieve → cite → refuse when unsupported) using TF-IDF retrieval + the
  `claude` CLI (already-approved ZAOS auth), in ~200 lines, zero secrets.
- **Dependencies:** `pypdf`, `scikit-learn`, `numpy` — resolved on demand by
  `uv run` (PEP-723 header). No model download, no `node`, no service.
- **Integration:** CLI + thin skill. No MCP, no hook.
- **Tested (2026-09-06)** — corpus: 3 hand-written `.md` notes with known claims
  + 1 real math PDF (Daubechies et al., arXiv:0706.4297). Evidence:
  `.runtime/eval/lit-review/`.
  - Q1 known-answer ("three CS conditions") → `GROUNDED`, correct, cited to the
    right file; $0.04, 7 s.
  - Q2 not-in-corpus ("fastMRI 2019 scan count / winner") → `INSUFFICIENT_CORPUS`,
    zero retrieval, $0 (no synthesis call).
  - Q3 false premise ("notes say CS-MRI needs uniform full-Nyquist sampling") →
    `INSUFFICIENT_CORPUS` + "E1 states the opposite" — refused the premise and
    flagged the contradiction.
  - `index` flags low extraction quality: the math PDF scored 0.667 (< 0.75
    threshold) and was flagged for `.md` conversion; the `.md` notes scored 0.91–0.99.
- **Known limitations:** PDF text extraction is the dominant failure mode (garbled
  fonts → number-for-letter substitution); the robust workflow is a curated `.md`
  corpus. TF-IDF retrieval is keyword-ish; no multi-hop, no reranking. Not yet run
  on a real external-literature corpus (that pilot is the deferred Human Lead item).
- **Disable/remove:** delete `.agents/skills/lit-review/`. Nothing else depends on it.
