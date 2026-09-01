# Project Intelligence SOP

## Purpose

The Project Intelligence Gate is a reusable, evidence-informed step before
architecture becomes expensive to change. It counters two opposite failures:
**AI-from-scratch bias** (inventing architecture, pipelines, or UI mainly from
agent preference) and **repository cargo cult** (copying a mature or popular
reference without testing its fit).

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
- **Codex / Local Data or Reference Agent:** safely inspects cloned references
  and local datasets, profiles/analyzes, runs bounded experiments, and produces
  evidence artifacts.
- **ECC-Zandi:** supplies reusable engineering/research workflows and quality
  doctrine.
- **Architecture Agent:** derives an architecture from Project Intelligence.
- **Implementation Agent:** builds the approved design.
- **Review Agent:** independently reviews when justified.

Pilot this SOP on GradTime before changing ECC-Zandi. A pilot may justify a
future `PROFILE_PATCH` only with evidence, lessons learned, and explicit Human
Lead approval; it creates no automatic framework change.
