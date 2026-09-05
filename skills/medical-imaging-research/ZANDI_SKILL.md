# Zandi skill metadata — Medical Imaging Research

- **Name:** medical-imaging-research
- **Category:** DOMAIN
- **Owner:** Zandi
- **Status:** DRAFT
- **Created:** 2026-09-05
- **Scope:** reusable medical-imaging research decisions — data semantics,
  preprocessing/leakage boundaries, exact evaluation-metric contracts
  (PSNR/SSIM/Dice-style), subject-level validation and external-cohort
  confirmation, and fair reconstruction/segmentation comparison. Does not
  own a project's own formula-specific inverse-problem mathematics.
- **Authorship:** written fresh in Zandi's own compact style, not copied
  from any upstream source. Seeded by real methodological decisions worked
  through during the Zandi Paper_Q1 project's Stage03 evaluation-contract
  design (generalized to remove all project-specific constants, formula
  names, scenario IDs, dataset names, and Stage identifiers before being
  written here).
- **Disposition on external material:** `REFERENCE_FOR_BUILD` — external
  content was read and used only to check citation quality and confirm
  which principles are established best practice; no upstream file was
  copied, adapted, or installed.
- **External source studied (reference-for-build only):**
  - Repository: `github.com/Aperivue/medsci-skills`
  - License: MIT
  - Inspected commit: `912f7e880aaa89a270aae37844c4e66be34d95c7` (default
    branch `main`, last pushed 2026-09-01)
  - Files studied: `skills/model-evaluation/SKILL.md`,
    `skills/preprocess-imaging/SKILL.md`, `skills/model-validation/SKILL.md`
  - Concepts/citations that informed this skill's principles: task-correct
    metric selection and metric-choice gating (Metrics Reloaded, Maier-Hein
    & Reinke et al., *Nat Methods* 2024); imaging-model reporting fit
    (CLAIM 2024, TRIPOD+AI, STARD-AI); imaging-specific data-stage leakage
    taxonomy (dataset-level normalizer fit on non-train data, a
    data-fitted transform run before the split exists, a subject's slices
    crossing splits) traced to the same class of failure Kapoor & Narayanan
    describe (*Patterns*, 2023) for leakage generally; patient-level split
    disjointness as the imaging-specific instance of grouped-split
    discipline.
  - Not adopted: the collection's remaining ~50 skills (literature search,
    grants, submission, meta-analysis, radiomics-ml, etc. — out of current
    scope); `uncertainty-imaging` (deployment/OOD-specific, no current
    Zandi need); the collection's `Read, Write, Edit, Bash` tool posture
    (this skill is guidance-only, matching Zandi's other DOMAIN skills).
- **Tested scenarios:** none yet — DRAFT, real Zandi project use is
  required before promotion, per Zandi's existing skill lifecycle. Do not
  promote merely because the studied external sources are well-cited.
- **Known limitations:** does not cover a project's own inverse-problem or
  signal-processing mathematics (stays project-local); does not cover
  deployment-time uncertainty/OOD machinery (out of current scope); has not
  been exercised against a real Zandi project yet.
- **Change history:** v0.1 created 2026-09-05 as DRAFT.
