# Literature corpus boundary — project-local setup

Apply this in the owning project (e.g. `projects/paper-q1-vis-tp`) once a Human
Lead has approved which papers may be held. Do not create it speculatively and do
not have an agent bulk-download paywalled material.

## Layout

```
projects/<project>/research/literature/
  .gitignore          # contains:  corpus/
  SOURCES.md          # one line per paper: cite, DOI/arXiv, license, how obtained
  corpus/             # the .md / .pdf files themselves — GITIGNORED, never committed
    <firstauthor><year>_<slug>.md      # preferred: converted + spot-checked
    <firstauthor><year>_<slug>.pdf     # only if extraction quality passes `litqa index`
  answers/            # litqa outputs — committed as evidence, human-citation-checked
    <question-slug>.md
```

## Rules

- **`corpus/` is gitignored.** The papers are never committed. `SOURCES.md` (the
  provenance ledger) and `answers/` (the derived evidence) are committed.
- **Prefer `.md`.** Run `litqa index research/literature/corpus` first; any file
  flagged `LOW_QUALITY_EXTRACTION` must be converted to clean markdown and
  spot-checked before it is trusted.
- **Provenance:** every file gets a `SOURCES.md` line — citation, DOI or arXiv id,
  licence (open-access / institutional / author's own), and how it was obtained.
- **Copyright:** open-access, the user's own work, or institutionally licensed
  only. An agent may fetch a *named* open-access URL the user provides; it must
  not crawl, scrape, or bulk-download.
- **Not authority:** `answers/*.md` are evidence. No claim enters the manuscript
  or a contract until a human has checked each `[E#]` against the cited source.
- **Project-local:** one corpus per project. There is no shared/global corpus.

## Pilot checklist (paper-q1-vis-tp)

1. Human Lead approves the paper list (or provides the PDFs).
2. Create the layout above; populate `corpus/` + `SOURCES.md`.
3. `litqa index` — confirm all files `OK` (convert any that are not).
4. Draft 8–10 questions from the existing bibliography with known answers.
5. `litqa ask` each; also answer each via the WebSearch+read baseline.
6. Score: citation accuracy (zero fabrication), correctness vs known, recall,
   cost, time. Record in `research/literature/PILOT_RESULTS.md`.
7. Decide: `lit-review` sufficient, or escalate to PaperQA2 (needs the API-key /
   Ollama decision).
