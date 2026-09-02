# Project Intelligence SOP

## Purpose

The Project Intelligence Gate is a reusable, evidence-informed step before
architecture and study design become expensive to change. It counters two
opposite failures: **AI-from-scratch bias** (inventing architecture, pipelines,
or UI mainly from agent preference) and **repository cargo cult** (copying a
mature or popular reference without testing its fit).

Zandi has now observed two further, related failures on real projects:

- a technically clean modelling-critical field was promoted before its
  semantic meaning was established (repaired by the semantic-readiness gates
  in `EFFICIENT_AGENTIC_ENGINEERING.md`); and
- a feature/model study was frozen before the complete resource and
  candidate-feature universe had been enumerated — the tournament was rigorous
  only inside an already-narrowed set, and an omitted original field later
  produced a large improvement. A related process gap: a clean rebuild
  declared its experimental scope complete without first recovering the
  predecessor project's design intelligence.

This gate therefore also exists to establish **universe completeness** and to
make **prior work** — legacy and professional-reference — an operational input
to project-specific study design before a scientific freeze, not merely a
discovery artifact. Sections F–H below add the corresponding gates.

Use the gate adaptively. It normally applies to substantial new products,
legacy clean rebuilds, ML/data-science systems, unfamiliar domains,
architecture-heavy work, projects with likely mature external implementations,
and substantial backend/frontend product design. It may be skipped or collapsed
for small bug fixes, obvious refactors, trivial bounded features, or low-value
research. If a substantial project skips Reference Intelligence or applicable
Dataset Intelligence, record an explicit rationale in its synthesis.

The goal is evidence-informed synthesis, not document production or a fixed
research quota. Counts below are scale guidance only: broad discovery may be
roughly 20–40 candidates, a shortlist 8–12, and deep study 3–6; collapse all
three when the domain is narrow.

## Canonical intelligence memory

Project Intelligence produces **durable design memory**, kept separate from
`PROJECT_STATE.md` (where the project is now) and `PROJECT_BLUEPRINT.md` (where
it intends to go and why). Prefer exactly one canonical synthesis per
applicable intelligence class, in `research/intelligence/` (or an
`intelligence/` tree with `legacy/`, `references/`, `data/`, and `domain/`
subfolders only when scale genuinely requires the split):

- `LEGACY_SYNTHESIS.md` — what predecessor work teaches (Section F).
- `REFERENCE_STUDY.md` — what relevant professional implementations teach
  (Section A).
- `DOMAIN_KNOWLEDGE.md` — authoritative rules, source-documented facts,
  empirical patterns, and explicitly unresolved assumptions.
- `DATASET_INTELLIGENCE.md`, `ADOPTION_LEDGER.md`, `PROJECT_SYNTHESIS.md` as
  defined in Sections B–D. For a sufficiently complex modelling project the
  data class may additionally carry **one** small machine-readable resource
  registry (Section B) beside the human synthesis; trivial projects do not
  need one.

Only create classes the project actually has. These are synthesis, not copied
repositories, activity logs, or transcripts; raw evidence may live elsewhere.
Avoid one report per experiment, repository, or dataset when a canonical
synthesis represents the knowledge safely. Do not mandate a file for a class a
project does not need. Once a synthesis is canonical, future agents consume it
first and reopen raw legacy or reference material only when the synthesis lacks
required detail, evidence conflicts, or a new decision genuinely requires it —
never to re-scan whole repositories.

## Focused high-intelligence passes

For a new project, a major rebuild, or a deep scientific / architectural
re-foundation, run the intelligence phase as **separate focused
High-capability passes** when project complexity justifies it, rather than one
overloaded discovery session that tries to discover, understand, design, and
implement at once. Canonical conceptual passes — use only those that are
material to the project:

- **Legacy project intelligence** (Section F)
- **Professional reference intelligence** (Section A)
- **Data / resource intelligence** (Section B)
- **Domain intelligence** where material (`DOMAIN_KNOWLEDGE.md`)
- **Architecture / scientific synthesis** (Section C and Section I)

Not every project uses every pass. Each pass has one bounded objective and its
output becomes durable project intelligence. Prefer a fresh High context per
large independent intelligence domain. Once the canonical synthesis for a pass
exists, later agents consume the synthesis first and do not re-scan the raw
source unless the synthesis is insufficient. High capability here is an
investment to reduce downstream cost and rework, not a standing operating
mode: after blueprint approval and freeze (Section I), routine work returns to
Medium (`MULTI_AGENT_ROUTING.md`, "Economic intent").

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

Consider the license of every candidate that influences implementation.

| Classification | Meaning |
| --- | --- |
| `REFERENCE` | Learn concepts and patterns. |
| `REUSE` | Reuse source/components only when the license permits it and attribution requirements are met. |
| `REIMPLEMENT` | Implement an idea or architecture pattern in original code. |
| `UNKNOWN_LICENSE` | Do not copy source. |

Public visibility is not permission to copy. Preserve required attribution;
avoid proprietary branding/assets; distinguish reusable components from visual
inspiration. Seek appropriate legal review when license interpretation is not
obvious or reuse has material consequences.

## B. Dataset Intelligence

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

Discipline:

- Do not infer a statistical missingness mechanism (MCAR / MAR / MNAR) without
  evidence; distinguish an observed pattern from a hypothesis.
- Do not prescribe blind global imputation for structural missingness.
- Any learned preprocessing operation must later be fit only on the appropriate
  training partition and applied to validation / test / OOT — never learned
  from future or holdout data.
- Dataset Intelligence may propose a processing strategy but must not silently
  execute scientific feature-selection decisions; those belong to the
  feature-family study (Section G) and the Human Lead.

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

For a substantial project, keep artifacts compact in `research/intelligence/`:

- `REFERENCE_STUDY.md` — shortlist, deep-study findings, patterns,
  strengths/weaknesses, license, and provenance.
- `DATASET_INTELLIGENCE.md` — privacy-safe aggregate evidence; data projects only.
- `ADOPTION_LEDGER.md` — decisions below.
- `PROJECT_SYNTHESIS.md` — what to build and why, challenge outcome, feasibility,
  sufficiency, external-data decision, architecture implications, and open questions.

Use `UI_REFERENCE_BOARD.md` only when the evidence volume warrants it. Do not
create further artifacts unless they add decision value.

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

For substantial projects, architecture is provisional until the Project
Intelligence Gate has enough evidence. The Architecture Agent receives product
goals, `PROJECT_SYNTHESIS.md`, `ADOPTION_LEDGER.md`, applicable dataset and
reference studies, and ECC-Zandi guidance. It selects the smallest coherent
architecture for the actual project; it must not mechanically merge discovered
patterns, templates, or repositories.

### Roles

- **Human Lead:** sets goals, preferences, constraints, and final decisions.
- **Zandi Orchestrator:** conducts public discovery, directs research,
  synthesizes and compares evidence, challenges assumptions, delegates bounded
  local study, and recommends the next Human Lead decision.
- **Implementation agent (Codex or Claude Code) / Local Data or Reference Agent:** safely inspects cloned references
  and local datasets, profiles/analyzes, runs bounded experiments, and produces
  evidence artifacts.
- **ECC-Zandi:** supplies reusable engineering/research workflows and quality
  doctrine.
- **Architecture Agent:** derives an architecture from Project Intelligence.
- **Implementation Agent:** builds the approved design.
- **Review Agent:** independently reviews when justified.

For a major design decision, the repository-aware agent returns informed
options, not a single silent choice — see `ZANDI_MASTER_WORKFLOW.md`, "Agent
as design collaborator". The Human Lead still owns the product/scientific
decision; the Orchestrator does not manually reproduce what the agent can
recover from the repository itself.

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

For modelling and analytics projects, before a feature contract is declared
complete or frozen, **every materially available predictor resource family
must carry an explicit, recorded disposition**. Conceptual flow:

> all available resources → semantic / point-in-time / leakage / identifier /
> support gates → complete admissible candidate universe → planned
> feature-family study → feature freeze.

Allowed dispositions, exactly one per family:

`ADMITTED` · `CANDIDATE_FOR_EXPERIMENT` · `DEFERRED` · `REJECTED` ·
`DIAGNOSTIC_ONLY` · `NOT_APPLICABLE`

A structural or context field used only for slicing or calibration still
appears in the universe with its disposition (for example `DIAGNOSTIC_ONLY`);
it may not be silently absent. A field is never required to enter a model
merely for ablation when a semantic, leakage, or point-in-time gate excludes
it — record `REJECTED` with the reason.

**A feature-family tournament is not evidence of universe completeness** unless
the candidate universe was established first. Enumerating families inside an
already-narrowed set — one domain, one source, one feature style — does not
satisfy this gate. Record the universe and its dispositions in
`DATASET_INTELLIGENCE.md` or `ADOPTION_LEDGER.md`; the feature contract
references it.

## H. Study-Design Freeze Gate

For empirical / model projects, a feature, model, or study freeze may be
called **FINAL** only when all of the following hold and are recorded:

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

Absent any of these, the freeze is **provisional**: it may still serve as a
working checkpoint, but it may not be cited as a final scientific result. This
gate is a Deep Gate; it does not apply to routine bounded work.

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

### Blueprint content

The blueprint carries only sections applicable to the project. A substantial
modelling / product project may include: product and scientific objectives and
claims; project boundaries; minimal repository architecture and canonical
folder responsibilities; data architecture and data / resource universe;
preprocessing and missing-data design; semantic assumptions; target / label /
estimand design; candidate feature universe, feature-engineering strategy, and
feature-family ablation strategy; model-candidate, hyperparameter/tuning,
temporal-split, validation / OOT, and calibration design; subgroup /
generalisation design; experiment stopping rules; reproducibility; production
architecture, model-artifact strategy, inference pipeline, API / service and
frontend / product integration; monitoring, drift detection, retraining /
update strategy, production data requirements; privacy / security; testing;
CI / release; rollback; observability; known limitations; staged implementation
plan; explicit decision gates.

For each major stage the blueprint states, where useful: OBJECTIVE · INPUTS ·
OUTPUTS · KEY DECISIONS · QUALITY GATES · DEPENDENCIES · STOP CONDITIONS ·
NEXT STAGE. This lets Medium agents execute a stage without the Orchestrator
reconstructing the design each sprint.

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

---

The GradTime rebuild is where these gates were validated: its clean-slate work
demonstrated both the semantic-readiness failure (Section A of the doctrine in
`EFFICIENT_AGENTIC_ENGINEERING.md`) and the feature-universe-completeness
failure (Sections F–H). A subsequent GradTime replay showed the same rebuild
would also have benefited from separate focused intelligence passes, deeper
dataset- and variable-level intelligence with explicit preprocessing and
missing-data recommendations, and a Human-approved blueprint before experiment
implementation and freeze; "Focused high-intelligence passes", the Section B
depth requirements, and Section I close that gap. Further changes to this SOP
require another concrete project failure, evidence, lessons learned, and
explicit Human Lead approval; they create no automatic framework change.
