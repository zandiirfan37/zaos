---
name: project-refoundation
description: Recover, modernize, acquire, or re-found a software, data, or AI project using only intelligence that can change the current decision. Use before greenfield work for material recovery, major restructuring, external-base evaluation, or a nontrivial build where prior art or data could change direction; not routine repairs.
---

# Project Re-foundation

Use this branchable workflow after the project intelligence governance route is
justified. Preserve project-local authority and the normal task loop. Do not
turn it into a fixed legacy → references → data → blueprint sequence.

## Control loop

`TRIAGE → SELECT TRACKS → CONVERGE → BOUNDED SPRINT → VERIFY → COMMIT →
UPDATE STATE → DECIDE AGAIN`

Triage is normally required for material recovery. All subsequent intelligence
tracks are zero-or-more and conditional. Stop when additional investigation is
unlikely to change the next decision.

## Triage

Establish only enough to choose direction: actual goal and current user
objective; visible assets and important resources; runnable/non-runnable state;
architecture shape; Git/history state; principal failures or debt; and likely
recovery mode.

Choose or present the smallest justified mode:

`REPAIR_IN_PLACE` · `REBUILD_CLEAN` · `ADOPT_EXTERNAL_BASE` ·
`HYBRID_REBUILD` · `EXTRACT_AND_ARCHIVE` · `GREENFIELD_FROM_REFERENCES` ·
`ABANDON`

Do not rebuild merely because code is unattractive. Repair in place when
working seams, tests/contracts, and compatibility value outweigh the isolated
defect. Prefer a clean rebuild when the foundation cannot meet required
constraints, interfaces are unknown or untestable, dependencies are
irreparably unsafe/obsolete, or incremental repair retains more accidental
complexity than it removes. Record material rationale, compatibility duties,
and rollback/migration implications locally.

When Human intent for a `REBUILD_CLEAN` or `HYBRID_REBUILD` is "best current"
(modernize onto the strongest available foundation, not merely repair), the
following become conditional expectations rather than a separate mode: a
targeted internal-evolution search across predecessor material, professional-
reference intelligence, invoking `project-architecture` before material
structural creation or change, and establishing data ownership/migration
design before material data mutation. Use `project-architecture`'s
early-clean-home threshold to time the new repository rather than waiting for
every intelligence track to finish. Do not force these tracks for a plain
`REPAIR_IN_PLACE`.

## Select only relevant intelligence tracks

Tracks may be read-only and parallel only if independently justified. They
must converge to one writer and one current direction.

### Legacy intelligence

Use when predecessor/current historical material can change the decision.
Recover useful architecture, components, experiments/results, bugs and
lessons, prior decisions, data knowledge, and hazards not to repeat. Give each
material finding one compact disposition:

`ADOPT` · `ADAPT` · `RETEST` · `DEFER` · `REJECT` · `OBSOLETE`

Create a canonical synthesis only if the pass occurred and has durable value.
Consume it first; do not repeatedly reread the legacy tree unless a named
unresolved decision requires it.

### Professional reference intelligence

Use when external implementations or conventions could improve a real design,
quality, or acquisition decision. Search and study only what is relevant. A
reference can be:

`LEARN_ONLY` · `BORROW_PATTERN` · `ADOPT_COMPONENT` · `MAJOR_ADOPTION` ·
`USE_AS_BASE` · `REJECT`

Major adoption and use-as-base are allowed when justified; when either is a
realistic candidate, make that reference decision before committing heavily
to a custom architecture (see `project-architecture`'s reference-timing rule).
Before acquiring a
base or major component, assess license, maintenance/activity, architecture,
tests, security, dependency/runtime burden, data assumptions, extension
points, goal mismatch, and adaptation versus rebuild cost. Do not permanently
clone large repositories for study; use disposable temporary inspection when
appropriate.

Discovery is not a stars contest: catalog only candidates that could change the
direction, then deepen the promising few. Include the applicable model-weight
and dataset license/access terms, project organization and documentation,
deployment/performance fit, portability, known weaknesses, and maintenance
burden. A final direction may deliberately combine upstream roles — for
example one product flow, another architecture pattern, a third evaluation
technique, and an independently adopted library/data source — if every adopted
piece has a clear role and integration cost. Do not build a Frankenstein merely
to preserve every promising idea.

When this intelligence has durable value, retain the smallest project-local
sequence that makes candidates, dispositions, constraints, and synthesis
auditable. Number ordered research artifacts when it helps navigation (for
example `research/01_repo_catalog.md`, `02_component_matrix.md`, and
`03_adoption_decisions.md`); combine stages or use a single direction note when
that is clearer. For every material influence, record its source, disposition,
borrowed/adopted role, relevant constraints, intentional departures, and reason.
Git remains history; these notes explain the decisions.

Reference work must become a concrete delta, not a catalogue:

`KEEP` · `REPLACE` · `ADOPT` · `ADD` · `REMOVE` · `RETEST` · `DEFER`

Every material recommendation connects to an actionable change or is explicitly
deferred.

### Existing data / resource intelligence

Use when local data/resources affect the plan. Inspect only as needed:
inventory/schema, grain, keys/linkage, labels/targets, semantic meaning,
temporal availability, quality/missingness, leakage, privacy/fairness, and
resource opportunity. Escalate to row-level investigation only when aggregate
evidence cannot resolve a concrete decision. Keep sensitive records local.

Decide canonical data ownership/target layout and its manifest/config/path
contract early and cheaply; do not physically move large datasets merely for
cleanliness — move only once a concrete trigger exists and migration impact
is understood (see `project-architecture`'s data-architecture section).

### Data-source discovery / acquisition

Use when required data does not exist locally. First define what data is
actually needed. Assess candidate public datasets, institutional/internal
sources, databases, APIs, repositories, or appropriate synthetic fixtures.
For each viable candidate record source, scope/content, license/access,
provenance, quality/limits, fit, acquisition cost, and privacy/security
constraints. Recommend `BEST_SOURCE` or `SOURCE_SET` plus an acquisition/access
plan. Never require data to already be local.

### Domain or other intelligence

Use only when specialized evidence changes correctness, safety, scientific, or
operational requirements. Do not load unrelated skills or deep references by
default.

## Converge and execute

When evidence is sufficient, record a compact `PROJECT_DIRECTION.md` only if
it has durable decision value. It is an evolvable blueprint, not a prison: mark
what is known/locked enough to start separately from what remains open to
upstream discovery, data reality, implementation evidence, benchmarks, UX, or
Human Lead direction. It should state, as applicable:

`MISSION · RECOVERY/BUILD MODE · WHAT EXISTS · KEEP · ADOPT · REPLACE · ADD ·
REMOVE · DATA PLAN · OPEN RISKS · BLOCKERS · NEXT 1–3 DECISIONS · NEXT BOUNDED
SPRINT`

Invoke `project-architecture` before material structural creation or change,
rather than deriving architecture inline here. Do not create numbered
intelligence folders or empty artifacts when they do not carry a durable
decision. Project truth
remains in `AGENTS.md`, `PROJECT_STATE.md`, direction/briefs when needed, and
relevant locks/contracts. A permanent giant `PROJECT_BLUEPRINT.md` is not the
default. Use an explicit, scope-bound Blueprint/freeze only when locking is
valuable for preregistration, irreversible migration, release,
security/privacy, compliance, or a comparable consequential gate.

Execute one coherent sprint, verify proportionately, inspect the meaningful
result, commit when authorized, update `PROJECT_STATE.md` for meaningful state
change, and choose the next decision. Reopen only the track that could change
it.

## Council and handoff

Use Ask the Council only after evidence leaves a consequential, credible
choice: repair versus rebuild, external base versus custom work, major
architecture, irreversible migration, scientific validity, or security/release
assurance. Do not council routine work.

When asked for a project handoff, generate—not commit—a compact 1–3k-token
view from `AGENTS.md`, `PROJECT_STATE.md`, `PROJECT_DIRECTION.md` if present,
the active stage/sprint brief if present, relevant locks/contracts only, and
Git status/recent log. Include:

`PROJECT / ROOT · HEAD · MISSION · CURRENT STATE · CURRENT ARCHITECTURE ·
IMPORTANT DECISIONS / LOCKS · LAST COMPLETED WORK · ACTIVE BLOCKERS · DO NOT
TOUCH · NEXT RECOMMENDED SPRINT · FILES NEXT ORCHESTRATOR SHOULD READ`

It is an ephemeral orientation view, never authoritative project state. Defer a
helper script until repeated real use demonstrates a need.
