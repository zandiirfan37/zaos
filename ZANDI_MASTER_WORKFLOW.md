# Zandi Master Workflow

Zandi is an AI Engineering Workbench: a local workspace where a Human Lead, the
ChatGPT Orchestrator, and two peer implementation/review agents — Codex CLI and
Claude Code CLI — collaborate on bounded, reviewable engineering work. See
`MULTI_AGENT_ROUTING.md` for roles, model routing, handoff, and concurrency.

## Workspace model

- `frameworks/` contains reusable engineering frameworks and their adapters.
- `projects/` contains independent project repositories and their artifacts.
- `runtime/` contains local runtime support such as browser and dependency
  caches; it is not a project deliverable.
- `instructions/` contains Zandi-owned, human-readable operating guidance.

The Zandi root is intentionally behaviorally non-Git. Each framework and
project owns its own Git repository, history, status, and remote policy. Check
the target repository before changing it; never assume root-level Git commands
apply to the workspace.

## Standard workflow

1. Inspect the target project: read `AGENTS.md`, `PROJECT_STATE.md`, `git status`
   and current HEAD, and the contract(s) relevant to the task before starting.
2. Choose the smallest relevant framework guidance.
3. For substantial work, complete the adaptive Project Intelligence Gate before
   treating architecture as stable; see `PROJECT_INTELLIGENCE_SOP.md`.
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

Routine bounded work runs a single fast lane, not a diagnose-then-implement
relay: read `PROJECT_STATE.md` → locate the relevant contract/blueprint
phase → identify the ECC gates the task type triggers → implement → test and
verify → update `PROJECT_STATE.md` on a meaningful transition → local commit.
When the same agent can safely diagnose and implement one bounded sprint, it
does both.

The implementation/review agent owns quality, not just literal execution. It
detects violations of the applicable scientific, semantic, temporal,
provenance, privacy/security, and engineering gates within its assigned
scope — deriving them from ECC-Zandi governance (see
`EFFICIENT_AGENTIC_ENGINEERING.md`, "Task-triggered quality gates" and
"Agent quality ownership") — and stops to escalate only on a material,
unresolved blocker. In particular, no modelling-critical field is promoted
on technical checks alone; semantic evidence and permitted modelling use are
required.

A **deep gate** (independent audit, added diagnostic stage, stronger review)
is used only when risk or ambiguity earns it: a new dataset or source; a new
target or label; a changed estimand; unresolved semantics; opening a sealed
test; a production-science, privacy, or security boundary; a major
architecture change; a feature, model, or study-design freeze called final;
declaring a legacy rebuild's experimental scope complete; or a release or
destructive change. It is not the default. The study-freeze and
intelligence-recovery gates are defined in `PROJECT_INTELLIGENCE_SOP.md`
(Sections F–H).

An audit must have a concrete decision it can change. If existing evidence
already establishes that decision, consume it rather than rerunning
discovery. Avoid repo rediscovery, repeated semantic audits after a gate is
established, and audit-report-prompt loops.

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

### Fast lane stays fast

These intelligence, universe, and freeze gates never require a routine parser
fix, a bounded code change, or a single-family ablation to inspect legacy
projects, study external repositories, re-enumerate the resource universe, or
redesign architecture. Task-triggered scope still governs; the deep gates
activate only when their decision is material.

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

Architecture and review depth match uncertainty and risk; the workflow may
collapse or expand. A small fix may be request → implementation → test →
report. A bounded feature may add a short plan and review when useful. A
substantial or ambiguous project normally uses goal → Project Intelligence
(reference, dataset when applicable, and opportunity synthesis) → project/legacy
evidence → ECC-Zandi guidance → architecture synthesis → Orchestrator challenge
→ Human Lead approval → implementation → validation → independent review when
justified. The gate is defined in `PROJECT_INTELLIGENCE_SOP.md`; skipping a
substantial project's reference or applicable dataset intelligence requires an
explicit rationale. For modelling and analytics projects the same SOP adds a
read-only legacy design-intelligence recovery pass, an explicit disposition
for every materially available predictor resource family, and a study-design
freeze gate before any feature or model freeze is called final (Sections F–H).
High-risk scientific, security, or data work uses stronger gates appropriate
to its risk.

The substantial-project flow is an adaptive reference, not a bureaucratic
pipeline. Do not require Terra High, architecture documents, independent
review, or multiple approvals when they do not materially improve the outcome.

## Multi-agent execution

Codex CLI and Claude Code CLI are peer implementation/review agents; Codex is
the primary implementer when available and Claude Code is the backup/takeover
implementer and independent reviewer. Only one agent is the active writer in a
working tree at a time. Handoffs cross at a clean boundary — Git status, diff,
tests, and a DONE/IN_PROGRESS/REMAINING split — with the repository, contracts,
tests, and evidence as the shared source of truth. Details, model routing, and
the Claude operating budget are in `MULTI_AGENT_ROUTING.md`.
