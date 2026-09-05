# Zandi Master Workflow

Zandi is an AI Engineering Workbench: a local workspace where a Human Lead, the
ChatGPT Orchestrator, and two peer implementation/review agents — Codex CLI and
Claude Code CLI — collaborate on bounded, reviewable engineering work. See
`MULTI_AGENT_ROUTING.md` for roles, model routing, handoff, and concurrency.

## Workspace model

- `.agents/frameworks/` contains reusable engineering frameworks and their adapters.
- `projects/` contains independent project repositories and their artifacts.
- `.runtime/` contains local runtime support such as browser and dependency
  caches, plus engine (Codex/Claude) state; it is not a project deliverable.
- `.agents/instructions/` contains Zandi-owned, human-readable operating guidance.

The Zandi root is intentionally behaviorally non-Git. Each framework and
project owns its own Git repository, history, status, and remote policy. Check
the target repository before changing it; never assume root-level Git commands
apply to the workspace.

## Standard workflow

1. Inspect the target project: read `AGENTS.md`, `PROJECT_STATE.md`, `git status`
   and current HEAD, and the contract(s) relevant to the task before starting.
2. Choose the smallest relevant framework guidance.
3. For substantial work, complete the adaptive Project Intelligence Gate before
   treating architecture as stable; for a new project, major rebuild, or
   re-foundation, converge the applicable intelligence streams into one
   Human-approved `PROJECT_BLUEPRINT.md` before substantial implementation or a
   FINAL freeze. See `PROJECT_INTELLIGENCE_SOP.md` (Sections A–J).
4. Plan and agree scope before material changes.
5. Implement locally, validate proportionately, update `PROJECT_STATE.md` when
   the sprint changes project state, and inspect the diff.
6. Commit only inside the target repository when requested; the `PROJECT_STATE.md`
   update normally rides in the same commit that establishes the new state.
7. Report results, risks, and framework lessons learned.

Global configuration, framework changes, remote actions, deployment, secrets,
and destructive migrations remain explicit approval boundaries.

## Canonical project state

Every active Zandi project SHOULD maintain exactly one canonical
`<project-root>/PROJECT_STATE.md` — the compact, current-state answer to *where
is the project now*. It is tracked in the project's Git repository, human- and
agent-readable, and references deeper files by path. It is **not** an activity
log and **not** a replacement for Git history, contracts, research evidence, or
intelligence reports. Template: `templates/PROJECT_STATE.template.md`.

Do not maintain both `PROJECT_STATE.md` and a standing `PROJECT_HANDOFF.md`.
`PROJECT_STATE.md` is canonical; a `PROJECT_HANDOFF.md` is generated only when a
specific external handoff needs one.

New projects are initialized with `AGENTS.md` and `PROJECT_STATE.md`. `AGENTS.md`
carries the state-maintenance rule; a project `CLAUDE.md`, when used, stays a
thin adapter to `AGENTS.md` and does not duplicate `PROJECT_STATE` governance.

### Update triggers

Update `PROJECT_STATE.md` on a meaningful state transition: a substantive sprint
completes; a phase transition; a milestone or gate state change; a blocker found
or resolved; a scientific/product readiness change; an active contract or
governing decision change; a change to the next authorized sprint; a significant
implementation-agent handoff; a project pause, milestone freeze, or release.

Do not update it for typo fixes, routine test reruns, exploratory commands,
minor in-sprint refactors, or edits that do not change project state.

### Definition of Done

For any sprint that changes project state, "done" means: implementation → relevant
tests → verification → update `PROJECT_STATE.md` → diff review → commit. This is
part of the normal Definition of Done — the Human Lead does not need to request
the `PROJECT_STATE.md` update in each sprint prompt. If work is intentionally
uncommitted or interrupted before a safe boundary, do not mark it complete;
`PROJECT_STATE.md` may record it as `IN_PROGRESS` only when that adds handoff
value.

## Fast lane and agent quality ownership

The engineering doctrine — fast lane, deep gate, agent quality ownership,
task-triggered gates, diff-first review, and audit stop conditions — is
`EFFICIENT_AGENTIC_ENGINEERING.md`. In Zandi terms:

**Fast lane** (routine bounded work): read `PROJECT_STATE.md` → the relevant
`PROJECT_BLUEPRINT.md` stage or contract phase → the ECC gates the task type
triggers → implement → test and verify → update `PROJECT_STATE.md` on a
meaningful transition → local commit. One agent diagnoses and implements a
bounded sprint; do not split the two. No modelling-critical field is promoted
on technical checks alone — semantic evidence and permitted modelling use are
required.

**Deep gate** (only when risk or ambiguity earns it): a new dataset, source,
target, label, or estimand; unresolved semantics; opening a sealed test; a
production-science, privacy, or security boundary; a major architecture change;
a feature / model / study-design freeze called final; declaring a rebuild's
experimental scope complete; a release or destructive change. The intelligence,
universe, freeze, and blueprint gates are `PROJECT_INTELLIGENCE_SOP.md`
(Sections F–J). An audit must have a concrete decision it can change; if
existing evidence already establishes that decision, consume it rather than
rerunning discovery.

### Agent as design collaborator

For deep-gate design work the implementation/review agent is not only a code
executor. Using its direct repository access it may be assigned to
investigate, synthesise, propose architecture or study design, and compare
options — then implement and validate the approved choice. For a major design
decision it returns a compact envelope, not a transcript:

> STATUS · EVIDENCE FOUND · CURRENT DESIGN STRENGTHS · CURRENT DESIGN GAPS ·
> VIABLE OPTIONS · RECOMMENDED OPTION + WHY · RISKS / LIMITATIONS · WHAT NOT
> TO DO · IMPLEMENTATION / EXPERIMENT PLAN · PROJECT_STATE · COMMIT · NEXT
> SINGLE SPRINT.

The agent must not silently make a product or scientific decision that belongs
to the Human Lead; it must surface informed options so the Human Lead is not
required to invent every option personally and the Orchestrator need not
manually reproduce what a repository-aware agent can recover. Preferred flow
for complex design: human insight → bounded investigation request → agent
repository synthesis → Orchestrator + Human Lead decision → implementation.
Routine fast-lane work keeps its concise report (`PROMPT_EXAMPLES.md`); this
richer envelope is only for material design or freeze decisions.

The Orchestrator frames scope and selects the applicable resource-intelligence
profile(s) — `STRUCTURED_RECORDS`, `TEXT_CORPUS_RETRIEVAL`, `VISUAL_MEDIA`,
`INTERACTIVE_ENV_AGENTIC`, or a composition (`PROJECT_INTELLIGENCE_SOP.md`,
Section J). The High agent owns the archetype-specific technical and scientific
investigation the profile defines; the Orchestrator does not need to hold every
archetype's methods personally, and is not the sole technical architect.

### Fast lane stays fast

These intelligence, universe, and freeze gates never require a routine parser
fix, a bounded code change, or a single-family ablation to inspect legacy
projects, study external repositories, re-enumerate the resource universe,
redesign architecture, re-run an intelligence pass, or reopen the blueprint.
Task-triggered scope still governs; the deep gates activate only when their
decision is material. After a blueprint freeze, routine work runs the Medium
stage-execution loop (`PROJECT_INTELLIGENCE_SOP.md`, Section I), not discovery.

### Prompt compression

A normal sprint prompt states the bounded objective, any important
scientific or product constraint, and any exceptional prohibition. It does
**not** restate standard ECC quality checks — the agent derives those from
repository governance. The Orchestrator is not a prompt compiler for routine
gates. Canonical pattern (see `PROMPT_EXAMPLES.md`):

> Execute `<bounded objective>` from current `PROJECT_STATE.md` and active
> contracts. Apply all relevant ECC gates automatically. Own implementation,
> validation, state update, and local commit. Escalate only material
> blockers.

## Adaptive architecture

Repository, module, package, service, and folder architecture must be derived
from the actual project, not inherited mechanically. Synthesize it from:

1. product and domain goals;
2. scientific or research requirements where applicable;
3. security, privacy, and data constraints;
4. real capability and domain boundaries;
5. project scale, expected evolution, maintainability, and testability;
6. runtime and deployment needs where relevant;
7. ECC-Zandi engineering guidance; and
8. relevant repo-study or legacy-analysis evidence.

Do not mechanically copy a legacy tree, framework template, ECC example,
external repository, previous Zandi project, or an Orchestrator suggestion.
Repo study and legacy analysis establish what must be preserved: valuable
behavior, requirements, constraints, failures, comparable evidence, and parity
expectations. They do not determine how a new implementation is organized.
A legacy architecture is retained only when it independently remains the best
fit for current requirements.

For a clean rebuild, preserve valid requirements, behavior, scientific
semantics, product contracts, evidence, provenance, parity expectations, and
operational knowledge. Do not automatically preserve source-tree shape,
numbered pipeline stages, historical module boundaries, runtime or deployment
assumptions, framework choices, or folder conventions.

> **Legacy defines knowledge and parity requirements. The new product earns
> its own architecture.**

### Complexity and workflow depth

Complexity must pay rent. Create directories, packages, layers, services,
adapters, interfaces, abstractions, framework components, or infrastructure
only for a concrete current responsibility or a clearly justified near-term
one. Avoid architecture cosplay, empty package forests, speculative
abstractions, premature service decomposition, enterprise layering for small
projects, diagram-matching directories, and patterns adopted only because a
framework demonstrates them. Prefer the smallest architecture with correct
boundaries that remains understandable, testable, and safe to evolve.

Architecture and review depth match uncertainty and risk. A small fix is
request → implement → test → report. A bounded feature may add a short plan and
review. A substantial or ambiguous project uses:

> goal → Project Intelligence (reference, archetype resource intelligence, and
> opportunity synthesis) → project / legacy evidence → ECC-Zandi guidance →
> architecture synthesis → Orchestrator challenge → Human-approved
> `PROJECT_BLUEPRINT.md` → implementation → validation → independent review when
> justified.

The gate is `PROJECT_INTELLIGENCE_SOP.md`. Skipping a substantial project's
reference or applicable resource intelligence needs an explicit rationale. For
a new project or re-foundation, run legacy, professional-reference, resource
(under the archetype profile that fits — Section J, not a tabular checklist by
default), and domain intelligence as separate focused High passes where
complexity justifies, converging into the blueprint before substantial
implementation. After blueprint freeze, routine stage execution returns to
Medium: `PROJECT_STATE` → blueprint stage → contracts → ECC gates → implement →
test → evidence → `PROJECT_STATE` → commit; broad discovery repeats only when
new evidence invalidates the blueprint. Modelling projects add the
legacy-recovery, resource-universe, and study-design-freeze gates (F–H).
High-risk scientific, security, or data work uses stronger gates.

The substantial-project flow is an adaptive reference, not a bureaucratic
pipeline. Do not require Terra High, architecture documents, independent
review, or multiple approvals when they do not materially improve the outcome.

## Multi-agent execution

Roles, model routing, handoff, concurrency, and the Claude operating budget are
`MULTI_AGENT_ROUTING.md`. Core rule: one active writer per working tree;
handoffs cross at a clean boundary — Git status, diff, tests, and a
DONE / IN_PROGRESS / REMAINING split — with the repository, contracts, tests,
and evidence as the shared source of truth.
