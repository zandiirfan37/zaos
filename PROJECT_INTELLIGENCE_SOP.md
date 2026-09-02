# Project Intelligence SOP

## Purpose

The Project Intelligence Gate is a reusable, evidence-informed step before
architecture and study design become expensive to change. It counters
**AI-from-scratch bias** (inventing architecture, pipeline, or UI mainly from
agent preference) and **repository cargo cult** (copying a mature reference
without testing its fit), and it makes **prior work** — legacy and
professional-reference — plus **resource-universe completeness** operational
inputs to project-specific design before any freeze.

The concrete project failures that produced each gate below (semantic
readiness, feature-universe completeness, legacy recovery,
intelligence-to-blueprint, archetype generality) are recorded in
`VALIDATION_LEDGER.md`; this SOP states only the current operating model.

Use the gate adaptively. It normally applies to substantial new products,
legacy clean rebuilds, ML/data-science systems, unfamiliar domains,
architecture-heavy work, and projects with likely mature external
implementations. It may be skipped or collapsed for small bug fixes, obvious
refactors, trivial bounded features, or low-value research. If a substantial
project skips Reference Intelligence or applicable Resource Intelligence,
record an explicit rationale in its synthesis.

The goal is evidence-informed synthesis, not document production or a research
quota. Counts are scale guidance only: broad discovery ~20–40 candidates, a
shortlist ~8–12, deep study ~3–6; collapse all three when the domain is narrow.

## Canonical intelligence memory

Project Intelligence produces **durable design memory**, separate from
`PROJECT_STATE.md` (where the project is now) and `PROJECT_BLUEPRINT.md` (the
recommended design and why). Keep **exactly one canonical synthesis per
applicable class**, in `research/intelligence/` (or an `intelligence/` tree
with `legacy/`, `references/`, `data/`, `domain/` subfolders only when scale
requires it). This table is the single authoritative artifact list — other
sections reference it, they do not restate it:

| Artifact | Job | Gate |
| --- | --- | --- |
| `LEGACY_SYNTHESIS.md` | what predecessor work teaches | F |
| `REFERENCE_STUDY.md` | what relevant professional implementations teach (plus a UI reference board only if evidence volume warrants) | A |
| `DOMAIN_KNOWLEDGE.md` | domain rules classified authoritative / source-documented / empirical / unresolved | H, I |
| resource-intelligence synthesis — `DATASET_INTELLIGENCE.md` for `STRUCTURED_RECORDS`, else `RESOURCE_INTELLIGENCE.md` | what our own data / corpus / media / tools are and what they support | B, G, J |
| `ADOPTION_LEDGER.md` | per-pattern `ADOPT` / `ADAPT` / `REIMPLEMENT` / `REJECT` / `DEFER` decisions with benefit, cost, risk | D |
| `PROJECT_BLUEPRINT.md` | the convergence: recommended design, options, staged plan | I |

A project that runs the gate but does **not** need a full blueprint (smaller
scope) may record the convergence in a compact `PROJECT_SYNTHESIS.md` instead —
never both. A sufficiently complex project may add **one** machine-readable
registry beside the resource synthesis (Section J); trivial projects do not.

Only create classes the project has. These are synthesis — not copied
repositories, activity logs, or transcripts; raw evidence lives elsewhere.
Avoid one report per experiment, repository, or dataset. Once a synthesis is
canonical, consume it first; reopen raw material only when it lacks required
detail, evidence conflicts, or a new decision genuinely requires it.

## Focused high-intelligence passes

For a new project, a major rebuild, or a deep scientific / architectural
re-foundation, run the intelligence phase as **separate focused
High-capability passes** when project complexity justifies it, rather than one
overloaded discovery session that tries to discover, understand, design, and
implement at once. Canonical conceptual passes — use only those that are
material to the project:

- **Legacy project intelligence** (Section F) — only when a predecessor exists.
- **Professional reference intelligence** (Section A) — only when mature
  external work plausibly exists.
- **Resource intelligence** (Section B via the applicable Section J profile) —
  only when the project has a non-trivial evidence base (records, corpus,
  media, or a tool / environment surface). A project with two heavy evidence
  archetypes may split this into one bounded sub-pass per profile rather than
  one overloaded pass.
- **Domain intelligence** (`DOMAIN_KNOWLEDGE.md`) — only when material.
- **Architecture / scientific synthesis** (Section C and Section I) — for any
  re-foundation.

The passes are conditional, not ceremonial. Not every project uses every pass;
a small project may collapse to a single synthesis pass. Each pass has one
bounded objective and its output becomes durable project intelligence. Prefer a
fresh High context per large independent intelligence domain. An optional
independent High review is used only before a high-risk or consequential
freeze. Once the canonical synthesis for a pass exists, later agents consume it
first and do not re-scan the raw source unless it is insufficient. High
capability here is an investment to reduce downstream cost and rework, not a
standing operating mode: after blueprint approval and freeze (Section I),
routine work returns to Medium (`MULTI_AGENT_ROUTING.md`, "Economic intent").

## A. Reference Intelligence

### Discovery

The Zandi Orchestrator searches broadly at web level for relevant open-source
repositories, official framework examples, research implementations, production
templates, architecture references, backend and frontend/UI references, and
useful papers or documentation. Do not clone everything.

Assess candidates by domain and conceptual relevance, production maturity,
architecture quality, testing discipline, CI/CD, documentation,
reproducibility, maintenance/activity, deployment practices, security,
observability, product UX where relevant, license, and complexity fit.
Stars and forks are weak signals; they never replace a quality assessment.

Create a short, reasoned shortlist, then delegate only high-value repositories
for local deep study. For product-facing work, treat frontend as a first-class
reference domain: study shells, navigation, dashboards, tables, filters, detail
views, charts, loading/error/empty states, responsive behavior, accessibility,
interaction density, design systems, component libraries, live demos, and E2E
patterns. Choose UI from usability, workflow, and technical fit—not novelty.

### Controlled deep study

Codex or a Local Reference Agent may clone or partially clone shortlisted
repositories into `/home/pc_pusaka/zandi/shared/reference-repos/<project>/`.
This cache is not a runtime dependency, is not automatically committed, may be
rebuilt or deleted, and must retain source URL and license provenance. Prefer
shallow, blobless, or sparse clone when sufficient.

Study implementation rather than README claims: module boundaries, data
pipelines, contracts, tests, CI, configuration, dependencies, databases and
migrations, APIs, error handling, security defaults, observability, model
lifecycle, deployment/containerization, frontend structure, E2E/accessibility,
responsive behavior, and release practices as relevant. Do not run installers,
hooks, deployments, MCP setup, global sync, or network services merely to
study a reference.

### Reference design synthesis

Reference study must not stop at "we read several professional repositories."
Where references are materially relevant, before a major architecture or
study-design freeze the synthesis must answer, for the patterns found: what
each solves; what is applicable here; what is overkill here; what our current
design is missing; and an explicit `ADOPT` / `ADAPT` / `DEFER` / `REJECT` per
pattern with rationale. The repository-aware agent turns references into a
project-specific design recommendation, not a catalogue. Not required for
routine bounded work.

### License and cleanroom discipline

Study external repositories to learn, not to disguise copying. Method: collect
candidates and check licences first; study architecture, features, tests, and
UX at pattern level; extract lessons; design an original Zandi version for our
requirements; implement from scratch unless license-compliant reuse is
explicitly approved; validate against Zandi requirements, not superficial
similarity; record sources, decisions, and attribution needs.

Classify the license of every candidate that influences implementation:

| Classification | Meaning |
| --- | --- |
| `REFERENCE` | Learn concepts and patterns. |
| `REUSE` | Reuse source/components only when the license permits it and attribution requirements are met. |
| `REIMPLEMENT` | Implement an idea or architecture pattern in original code. |
| `UNKNOWN_LICENSE` | Do not copy source. |

Public visibility is not permission to copy. Be scientifically and ethically
honest: preserve required attribution; never present copied work as original,
use proprietary code or assets, or violate a licence; distinguish reusable
components from visual inspiration. Seek appropriate legal review when license
interpretation is not obvious or reuse has material consequences.

## B. Dataset / Resource Intelligence

**Archetype scope.** This section is the **`STRUCTURED_RECORDS`** resource
profile (tabular and time-series records for prediction / analytics). Projects
whose primary evidence is a document corpus, visual media, or a tool /
environment surface use the matching profile in **Section J** instead of — or
composed with — this one, and skip the tabular specifics here that do not
apply. The progressive-inspection discipline, the disposition requirement
(Section G), and the "propose but do not silently decide" rule are common to
every profile.

For non-trivial datasets, perform Dataset Intelligence locally near the data
before locking model or product scope. Its purpose is to establish what the data
represents, what can responsibly be predicted or inferred, what exists at
decision time, which joins/domains are reliable, and whether additional data is
justified. Large or restricted data must not normally be uploaded wholesale to
the Orchestrator. The Implementation/Data Agent produces privacy-safe aggregate
evidence; sensitive row-level work stays local.

Use progressive inspection, stopping at the lowest level that answers the
decision:

| Level | Bounded work |
| --- | --- |
| 0 — Metadata | Files, formats, sizes, hashes, sheet/table names, schemas, columns, row counts, and provenance. |
| 1 — Aggregate profile | Missingness, cardinality, duplicate counts, coverage, target distribution/prevalence, aggregate distributions, and domain completeness. Do not report identifiable row values. |
| 2 — Relational/temporal | Entity/key map, join and orphan rates, cohorts, temporal/cutoff coverage, target timing, prediction-time feature availability, longitudinal density, drift, leakage candidates, and post-outcome variables. |
| 3 — Targeted local investigation | Investigate row-level anomalies only when aggregates cannot explain them; keep records local and out of Git, docs, prompts, and shared reports. |
| 4 — Model feasibility | Only when governance permits: simple and temporal baselines, ablation, calibration, information-value, and external-data incremental-value experiments. |

The analysis must explicitly answer, where applicable: the entity/population;
authoritative assets; target/outcome and reliable constructibility; temporal
unit and prediction cutoffs; identifiers; post-outcome, target-derived, and
split-only fields; sparse and longitudinally strong domains; reliable joins and
the origin of missingness; cohort/system changes; historical and active/product
population coverage; leakage; bias/coverage limits; scientifically valid and
invalid products; stronger projects supported by the same data; and whether
external data closes a real information gap.

### Dataset and variable depth

For modelling / data projects, inspect each material dataset and each
materially relevant variable or concept deeply enough to support downstream
preprocessing, missing-data, feature-engineering, and experimental-design
decisions — not only a surface profile.

At **dataset** level, record where applicable: source and provenance;
business / domain purpose; grain; key / linkage structure; temporal meaning;
cohort / time coverage; row / entity coverage; schema stability; duplicates;
missingness patterns; structural versus accidental missingness; source-specific
quality problems; joins and relationship cardinality; historical / version
semantics; point-in-time usability; leakage risk; privacy / identifier risk;
modelling roles; known limitations.

At **variable / concept** level, record where applicable: semantic meaning;
data type; unit / category domain; valid range; impossible or suspicious
values; cohort / source coverage; temporal stability; missingness rate and
pattern; whether missingness may itself carry information; semantic readiness;
point-in-time readiness; leakage / post-outcome risk; identifier / proxy risk;
subgroup / fairness considerations; raw modelling eligibility; candidate
feature-engineering transformations; potential interactions; recommendations
for preprocessing, imputation, missing-indicator, encoding, scaling /
normalisation, outlier treatment, rare-category strategy, and cutoff-specific
handling; candidate feature family; final disposition.

Also resolve, for a predictive / analytics project:

- **original vs engineered feature accounting** — every raw field is traced to
  admitted, transformed, or rejected; no raw field silently vanishes;
- **candidate feature families** and the **ablation opportunities** that would
  test each family's contribution;
- **target / label / estimand** definition and each variable's relationship to
  it (upstream cause, proxy, post-outcome, leakage);
- **split design and leakage surface** — split unit, temporal or grouped
  splits, and every field that could leak the outcome or the split;
- **evaluation implications** — what the data allows to be measured honestly
  (metric fit, calibration, subgroup breakdown, coverage);
- **production-data implications** — which resources and variables will exist,
  with the same semantics and point-in-time availability, at serving time.

Discipline:

- Do not infer a statistical missingness mechanism (MCAR / MAR / MNAR) without
  evidence; distinguish an observed pattern from a hypothesis.
- Do not prescribe blind global imputation for structural missingness.
- Any learned preprocessing operation must later be fit only on the appropriate
  training partition and applied to validation / test / OOT — never learned
  from future or holdout data.
- Resource intelligence may propose a processing strategy but must not silently
  execute scientific feature-selection decisions; those belong to the
  feature-family study, Section G, and the Human Lead.

### Optional resource registry

For a sufficiently complex modelling project, keep a small machine-readable
resource registry beside `DATASET_INTELLIGENCE.md` (exact format project-local)
in addition to the human synthesis. It should support fields such as:
`resource`, `dataset`, `variable/concept`, `source`, `grain`,
`semantic_status`, `PIT_status`, `coverage`, `missingness_pattern`,
`preprocessing_strategy`, `imputation_strategy`, `encoding_strategy`,
`outlier_strategy`, `feature_family`, `allowed_use`, `disposition`, and
`evidence/reference`. Its purpose is to stop resource families or variables
from silently disappearing and to let later implementation agents consume
decisions efficiently. Do not mandate it for trivial projects.

At completion, record both decisions without forcing optimism:

| Decision | Allowed values |
| --- | --- |
| `PROJECT_FEASIBILITY` | `GO`, `GO_WITH_GAPS`, `PIVOT`, `STOP` |
| `DATA_SUFFICIENCY` | `SUFFICIENT`, `SUFFICIENT_WITH_LIMITATIONS`, `NEED_EXTERNAL_DATA`, `INSUFFICIENT` |

## C. Project Opportunity Synthesis

The Orchestrator combines Human Lead goals, local dataset evidence, external
reference evidence, relevant domain research, and ECC-Zandi guidance. It must
challenge the initial concept, not merely optimize it. Consider whether to
preserve the **current goal**, add a justified **expansion**, **reframe** the
target/product, **pivot** to a more valuable project enabled by the same data,
or pursue **external enrichment**.

Compare reference assumptions with local evidence before adopting them. For
example, if successful references depend on activity trajectories but local
activity coverage is weak and academic history is strong, adapt around reliable
academic trajectories and test activity features with coverage-aware ablation;
do not reproduce the reference pipeline blindly. Architecture emerges from this
synthesis.

Keep intelligence artifacts compact and canonical — see "Canonical intelligence
memory" for the authoritative list. The challenge outcome, feasibility,
sufficiency, external-data decision, architecture implications, and open
questions land in `PROJECT_BLUEPRINT.md` (or `PROJECT_SYNTHESIS.md` for a
gate-without-blueprint project). Do not create further artifacts unless they
add decision value.

## D. Adoption Decisions

For each important pattern, record source/reference, pattern, benefit, cost,
risks, project fit, decision, and rationale. Use exactly one decision:

- `ADOPT` — use substantially as-is when justified and licensed.
- `ADAPT` — retain the core pattern but change it for project constraints.
- `REIMPLEMENT` — retain the idea while writing original code.
- `REJECT` — deliberately do not use it.
- `DEFER` — plausible later value, not justified now.

Do not add external data merely because it exists. Define the information gap,
then assess lawful/permitted use, compatible entity/time granularity, coverage,
maintenance cost, plausible incremental signal, and leakage, bias, and privacy
risk. Classify need as `NOT_NEEDED`, `OPTIONAL_ABLATION`, `RECOMMENDED`, or
`REQUIRED`; when feasible, support adoption with incremental-value or ablation
evidence rather than intuition.

## E. Architecture Handoff

For substantial projects, architecture is provisional until the gate has enough
evidence. The synthesis draws on the blueprint inputs (`PROJECT_BLUEPRINT.md`
or `PROJECT_SYNTHESIS.md`), `ADOPTION_LEDGER.md`, the applicable resource and
reference syntheses, and ECC-Zandi guidance, and selects the smallest coherent
architecture for the actual project — it must not mechanically merge discovered
patterns, templates, or repositories.

Roles are defined once in `MULTI_AGENT_ROUTING.md` §1. For a major design
decision the repository-aware High agent returns informed options, not a single
silent choice (`ZANDI_MASTER_WORKFLOW.md`, "Agent as design collaborator"); the
Human Lead owns the product/scientific decision and the Orchestrator does not
manually reproduce what the agent can recover from the repository.

## F. Legacy Design-Intelligence Recovery Gate

When a project replaces or rebuilds an existing one, a **read-only legacy
design-intelligence pass is a hard prerequisite before the new experimental or
architectural scope is declared complete**. Inventory and disposition of
legacy *data and assets* are governed by `LEGACY_MIGRATION_POLICY.md`; this
gate covers legacy *design and scientific intelligence*.

Recover from the predecessor(s) what is materially useful: architecture and
folder structure; datasets, features, targets, and labels; study design and
evaluation protocol; models tried; successful experiments; failed experiments
and why; known leakage / semantic / temporal problems; technical debt; and
untested ideas. Classify each recovered idea exactly once:

`ADOPT` · `ADAPT` · `RETEST` · `DEFER` · `REJECT` · `OBSOLETE`

The goal is a clean architecture that preserves scientific and engineering
intelligence — neither copying the legacy tree nor forgetting what it already
learned (`ZANDI_MASTER_WORKFLOW.md`, "Adaptive architecture"). Record the pass
in `LEGACY_SYNTHESIS.md`. Do not reopen the raw legacy repositories once that
synthesis is canonical unless it lacks required detail or a new decision
demands it.

## G. Resource / Feature Universe Gate

Before a project's resource or feature contract is declared complete or frozen,
**every materially available resource family must carry an explicit, recorded
disposition** — regardless of archetype. A "resource family" is a predictor
family for `STRUCTURED_RECORDS`, a corpus source for `TEXT_CORPUS_RETRIEVAL`, a
media source and its annotation set for `VISUAL_MEDIA`, and a tool, environment,
or external dependency for `INTERACTIVE_ENV_AGENTIC` (Section J). Conceptual
flow:

> all available resources → semantic / point-in-time / leakage / identifier /
> isolation / support gates → complete admissible universe → planned study or
> integration → contract freeze.

Allowed dispositions, exactly one per family:

`ADMITTED` · `CANDIDATE_FOR_EXPERIMENT` · `DEFERRED` · `REJECTED` ·
`DIAGNOSTIC_ONLY` · `NOT_APPLICABLE`

A structural or context field used only for slicing or calibration still
appears in the universe with its disposition (for example `DIAGNOSTIC_ONLY`);
it may not be silently absent. A field is never required to enter a model
merely for ablation when a semantic, leakage, or point-in-time gate excludes
it — record `REJECTED` with the reason.

**A feature-family tournament is not evidence of universe completeness** unless
the candidate universe was established first — and neither is an index built
from a convenient subset of corpus sources, nor a model trained on one image
source, nor an agent evaluated against one tool set. Enumerating candidates
inside an already-narrowed set — one domain, one source, one feature style —
does not satisfy this gate. Record the universe and its dispositions in the
resource-intelligence synthesis or `ADOPTION_LEDGER.md`; the feature or
resource contract references it.

## H. Study-Design Freeze Gate

This is the **empirical / model** freeze gate. A feature, model, or study freeze
may be called **FINAL** only when all of the following hold and are recorded:

- target semantics established (semantic-readiness gate passed);
- resource / feature universe established and every family dispositioned
  (Section G);
- legacy design-intelligence recovered and classified where a predecessor
  exists (Section F);
- relevant professional-reference patterns synthesised into a project-specific
  recommendation (Section A);
- domain knowledge classified — authoritative / source-documented / empirical
  / unresolved;
- temporal and evaluation protocol defined;
- ablation / model-selection plan defined;
- unresolved assumptions listed explicitly;
- for a new project, major rebuild, or re-foundation, the applicable
  intelligence streams have converged into a Human-approved
  `PROJECT_BLUEPRINT.md` (Section I).

Absent any of these, the freeze is **provisional** — a working checkpoint that
may not be cited as a final scientific result. This is a Deep Gate; it does not
apply to routine bounded work.

A non-empirical project (general software, or an agent evaluated by task-suite
rather than an estimand) has **no** study-design freeze. Its freeze is the
Blueprint freeze (Section I), checked against the applicable Section J profile
completeness dimensions plus the Section G dispositions.

## I. Blueprint Synthesis Gate

For a new project, major rebuild, or scientific / architectural re-foundation,
the applicable intelligence streams must converge into **one canonical
project-specific blueprint** (`PROJECT_BLUEPRINT.md`) before substantial
implementation resumes or a FINAL scientific / architecture freeze is claimed
(Section H).

The blueprint is not written from product goals alone. It explicitly
synthesises product goals + current resource / data intelligence + legacy
project intelligence where applicable + professional reference intelligence
where applicable + domain knowledge + known constraints + engineering /
scientific risks into the recommended project design. Repository-aware
High-capability agents are used before approval where a design question is
genuinely difficult (`ZANDI_MASTER_WORKFLOW.md`, "Agent as design
collaborator").

The synthesis agent normally returns: EVIDENCE BASE · PREDECESSOR / CURRENT
DESIGN STRENGTHS · PREDECESSOR / CURRENT DESIGN GAPS · 2–3 VIABLE DESIGN
OPTIONS where genuine alternatives exist · TRADE-OFFS · RECOMMENDED DESIGN ·
WHY · RISKS / LIMITATIONS · WHAT IS DELIBERATELY NOT ADOPTED · STAGED
IMPLEMENTATION PLAN. The Human Lead owns approval of material product and
scientific choices.

### Archetype-aware blueprint content

Blueprint completeness is **CORE + archetype module + project-local**.

**CORE (every blueprint):** product and, where applicable, scientific
objectives and claims; project boundaries; minimal repository architecture and
canonical folder responsibilities; the resource / evidence universe and its
Section G dispositions; key design decisions with rationale; risks and known
limitations; reproducibility; testing; privacy / security; and — where a
running product exists — serving architecture, monitoring, rollback, and
observability; a staged implementation plan; explicit decision gates.

**Archetype module (the stage spine and emphasis differ):**

| Profile | Blueprint stage spine |
| --- | --- |
| `STRUCTURED_RECORDS` | data contract → preprocessing / missing-data → feature universe and engineering → target / estimand → temporal or grouped split → model and tuning → calibration → validation / OOT → retraining / update |
| `TEXT_CORPUS_RETRIEVAL` | ingestion → parsing / extraction → chunking and metadata → indexing / embedding → retrieval and rerank → grounding / generation → evaluation (retrieval + faithfulness + answer) → serving and caching → tenancy / ACL → observability and feedback |
| `VISUAL_MEDIA` | acquisition → annotation and QA → split design → preprocessing and normalization → augmentation → training → evaluation (task metric + slices) → calibration / thresholds → serving and preprocessing parity → drift monitoring |
| `INTERACTIVE_ENV_AGENTIC` | tool contracts → state / memory → planning and stop conditions → permissions and sandboxing → eval environments → failure recovery → observability and tracing → cost / latency budgets → rollout and kill switch |

A composed project carries more than one spine (a RAG product has the
`TEXT_CORPUS_RETRIEVAL` spine plus the CORE serving / product stages).

**Project-local:** everything specific to this project (GradTime's cutoff
ladder, a tenant list, a class taxonomy).

For each major stage the blueprint states, where useful: OBJECTIVE · INPUTS ·
OUTPUTS · KEY DECISIONS · QUALITY GATES · DEPENDENCIES · STOP CONDITIONS ·
NEXT STAGE. This lets a Medium agent execute a stage from a short prompt —
`PROJECT_STATE` + the active stage + contracts — without the Orchestrator
reconstructing the design.

### Blueprint freeze

No project may claim a FINAL architecture / study-design freeze while an
applicable intelligence stream is materially incomplete. A blueprint-gated
freeze decision returns explicitly:

- `INTELLIGENCE_COMPLETE: YES / NO`
- `BLUEPRINT_SYNTHESIS_REQUIRED: YES / NO`
- `BLUEPRINT_READY_FOR_IMPLEMENTATION: YES / NO`

After Human approval and blueprint freeze, routine implementation flow is:
`PROJECT_STATE` → relevant blueprint stage → active contracts → applicable ECC
gates → implement → test → evidence → `PROJECT_STATE` → commit. Broad discovery
is not repeated unless new evidence materially invalidates or exposes
incompleteness in the blueprint. This gate is a Deep Gate; it does not apply to
routine bounded work and never forces a Fast-Lane task to re-run intelligence
or reopen the blueprint.

## J. Resource-Intelligence Profiles

Different project archetypes need different resource intelligence before the
blueprint. The global lifecycle is unchanged — legacy recovery (F), reference
study (A), domain classification, synthesis-first memory, High sessioning,
Human approval, blueprint synthesis (I), Medium execution, `PROJECT_STATE`,
contracts, and ECC quality ownership apply to every archetype. Only the
**resource-intelligence completeness model** is archetype-specific.

A High resource pass loads this preamble plus only its applicable profile
subsection(s) — not the other profiles.

**Composition.** A project declares the profile(s) that apply; most real
projects compose one **evidence** profile with a product / delivery shape. A
multi-tenant RAG assistant is `TEXT_CORPUS_RETRIEVAL` plus a service / app
product; a predictive product like GradTime is `STRUCTURED_RECORDS` plus a
service / app product; a vision classifier is `VISUAL_MEDIA` plus a service
product. When two evidence profiles are both material, run both — do not force
one label.

**Common to every profile.** Progressive inspection stopping at the lowest
level that answers the decision; privacy-safe aggregate evidence out, sensitive
detail local; every resource family carries a Section G disposition
(`ADMITTED` · `CANDIDATE_FOR_EXPERIMENT` · `DEFERRED` · `REJECTED` ·
`DIAGNOSTIC_ONLY` · `NOT_APPLICABLE`); nothing materially available is silently
absent; the intelligence **proposes** processing / retrieval / annotation /
tool strategy but does not silently make the scientific or product decision
that belongs to the Human Lead.

**Output format.** One canonical synthesis per class (Markdown), structured for
downstream retrieval, not polished prose: stable headings matching the profile
dimensions below; an explicit `STATUS_TOKEN: VALUE` at each decision; dense
tables over paragraphs; a short `DECISIONS` block near the top; a stable ID per
resource / variable / source / tool so the blueprint and later agents can
reference it. Where a registry earns its keep, keep **one** machine-readable
companion (JSON/YAML) keyed by that ID — a resource registry
(`STRUCTURED_RECORDS`), a corpus registry (`TEXT_CORPUS_RETRIEVAL`), an
image-source / annotation registry (`VISUAL_MEDIA`), or a tool registry
(`INTERACTIVE_ENV_AGENTIC`). The human executive summary is one short section.
Do not humanise every result; do not proliferate artifacts.

### J.1 `STRUCTURED_RECORDS`

Section B is this profile in full. Completeness dimensions: resource and
variable universe; provenance, grain, linkage; temporal semantics and
point-in-time availability; missingness pattern (distinguished from an unproven
mechanism) and structural vs accidental absence; preprocessing, imputation,
missing-indicator, encoding, scaling, outlier, and rare-category strategy;
feature-engineering opportunities and interactions; original vs engineered
feature accounting; candidate feature families and ablation opportunities;
target / label / estimand and each variable's relationship to it; split design
and leakage surface; identifier / proxy risk; cohort / regime stability;
evaluation implications; production-data implications; subgroup / fairness.
Decisions: `PROJECT_FEASIBILITY`, `DATA_SUFFICIENCY` (Section B).

### J.2 `TEXT_CORPUS_RETRIEVAL`

For RAG, assistant, search, and NLP-pipeline systems. A High pass resolves:

- **Corpus universe** — every source / collection / feed; ownership; licence
  and permitted use; sensitivity classification; volume and growth rate;
  format mix (PDF, HTML, office, scanned, tables, code); language mix; update
  and version cadence; which source is authoritative on conflict.
- **Document semantics and structure** — what each source means; document
  types; structural richness (headings, tables, figures, footnotes);
  boilerplate and navigation noise; near-duplicates and versioned duplicates;
  extraction-fidelity risk (scanned, OCR, complex layout); the natural atomic
  unit of a fact.
- **Chunking and representation** — natural retrieval unit per source; chunk
  boundary semantics; metadata available for filtering (source, date, section,
  entity, tenant, ACL); embedding-model fit to the domain vocabulary;
  multilingual handling.
- **Retrieval and grounding** — query classes the product must serve; expected
  answer types (extractive, synthesised, procedural, refusal); known hard
  query classes; freshness requirements; conflicting-source handling;
  citation / traceability requirement; what "grounded" means and how a claim
  maps to a chunk.
- **Tenant, security, and privacy boundaries** — multi-tenant isolation model;
  per-document ACL and retrieval-time authorization; PII / PHI / secret
  exposure risk in the corpus; prompt-injection surface in ingested content;
  retention and right-to-deletion.
- **Evaluation universe** — gold question / answer sets; retrieval metrics
  (recall@k, nDCG) feasibility; grounding / faithfulness evaluation;
  hallucination and refusal-correctness; answer-quality rubric; regression
  set; offline vs online; human-review loop.
- **Serving and cost** — latency budget across retrieve, rerank, generate;
  index size and refresh cost; token / compute cost per query; caching;
  degradation and fallback behaviour; model-provider dependency and change
  risk.
- **Leakage and contamination** — eval questions vs index / training
  contamination; documents postdating a question; tenant bleed in shared
  indexes.

Decisions: `CORPUS_SUFFICIENCY` (`SUFFICIENT` · `SUFFICIENT_WITH_GAPS` ·
`NEEDS_MORE_SOURCES` · `INSUFFICIENT`); `GROUNDING_FEASIBILITY`;
`TENANCY_MODEL`; per-source disposition.

### J.3 `VISUAL_MEDIA`

For image, video, and other visual-media models (classification, detection,
segmentation, reconstruction, generation). A High pass resolves:

- **Media universe** — every acquisition source, device, and sensor; capture
  conditions (lighting, resolution, sensor, compression, colour space); volume
  per source; source-linked confounds (a source that correlates with the
  label); synthetic vs real; licence and subject consent / privacy.
- **Content semantics** — what each image is; class taxonomy and definitions;
  label granularity (image, box, mask, keypoint, pixel); ambiguous and
  boundary classes; class prevalence and long tail; co-occurrence structure.
- **Annotation** — annotation provenance and tool; inter-annotator agreement
  and gold protocol; label noise and systematic annotator bias; missing or
  partial annotations; guideline stability over time; re-annotation needs.
- **Preprocessing and augmentation** — native resolution distribution;
  resize / crop / pad policy and aspect-ratio semantics; normalization stats
  (train partition only); which augmentations are label-preserving for this
  task and which destroy the signal; class-imbalance handling; test-time
  augmentation.
- **Splits and leakage** — split unit must be subject / patient / scene /
  session / device, not image; near-duplicate and burst-frame leakage;
  source / site leakage; temporal leakage; spatial leakage from overlapping
  tiles; label leakage via filename, EXIF, or capture order.
- **Evaluation** — metric fit (accuracy, mAP, IoU, Dice, PSNR / SSIM / FID);
  per-class and per-source breakdown; operating-point / threshold policy;
  calibration where probabilities are used; failure-mode taxonomy;
  distribution-shift slices; fairness across subject attributes.
- **Production-media implications** — inference input distribution vs training;
  on-device vs server; resolution, latency, throughput; preprocessing parity
  between train and serve; drift in capture conditions; human-in-the-loop
  review.

Decisions: `DATA_SUFFICIENCY`; `SPLIT_UNIT`; `ANNOTATION_READINESS`;
per-source and per-annotation-set disposition.

### J.4 `INTERACTIVE_ENV_AGENTIC`

For tool-using agents and autonomous / multi-agent systems. A High pass
resolves:

- **Tool and action surface** — every tool / API / function available;
  input / output contracts; side-effect class (read, reversible write,
  irreversible, external-visible, spend); rate limits and cost per call;
  failure and error semantics; idempotency; auth scope per tool.
- **Task and planning universe** — task types; decomposition patterns;
  expected trajectory length and branching; where planning is hard or
  ambiguous; success definition and stop conditions per task type; known
  failure and loop patterns.
- **State and memory** — state carried within and across sessions; memory
  store semantics; staleness and invalidation; context-window budget and
  retrieval of the agent's own memory; shared state for multi-agent cases.
- **Permissions and sandboxing** — privilege model; which actions require a
  human approval; execution sandbox and isolation; blast-radius limits; secret
  handling; prompt-injection and tool-output-injection surface;
  untrusted-content boundary.
- **Evaluation environments** — a deterministic or replayable eval
  environment; task suites and rubrics; success + safety + cost metrics;
  regression scenarios; offline simulation vs live; contamination between eval
  tasks and prompts / training; human grading loop.
- **Failure recovery and observability** — detection of stuck, looping, or
  diverging runs; retry, rollback, compensation; partial-failure handling;
  full-trajectory logging (prompts, tool calls, outputs, decisions);
  replayability; cost and latency observability; kill switch.
- **Cost and latency** — per-task token / tool / compute budget; tail-latency
  behaviour; parallelism; provider dependency and change risk.

Decisions: `TOOL_SURFACE_READINESS`; `EVAL_ENV_AVAILABILITY`;
`AUTONOMY_BOUNDARY`; per-tool and per-environment disposition.

### J.5 Software / product without a learned component

General software, API, and web-app projects have no evidence profile. The gate
collapses toward reference study (A), domain classification, and the Section I
blueprint. Section G still applies — the data model, integrations, and
external-service dependencies are resource families and none may silently
disappear — though it is usually light. Section H does not apply (see
Section H). Execution guidance is the ECC-Zandi route in
`frameworks/ecc/zandi-profile/prompts/`.

### Adding a profile

A new profile is justified only by a real project whose resource intelligence
does not fit an existing profile, plus lessons learned and Human Lead approval
(`FRAMEWORK_IMPROVEMENT_LOOP.md`). If the profile set grows past roughly six,
extract Section J to `instructions/profiles/` as one compact file per profile;
until then, keeping them here keeps the authority single and the drift low.

---

These gates were validated on the GradTime rebuild and refined by two later
audits — intelligence-to-blueprint, then archetype generality; the evidence and
rationale are in `VALIDATION_LEDGER.md`. Changing this SOP requires another
concrete project failure, evidence, lessons learned, and explicit Human Lead
approval — no automatic framework change.
