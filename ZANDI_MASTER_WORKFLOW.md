# Zandi Master Workflow

Zandi is an AI Engineering Workbench: a local workspace where a human,
ChatGPT, and Codex collaborate on bounded, reviewable engineering work.

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

1. Inspect the target project and its Git status.
2. Choose the smallest relevant framework guidance.
3. For substantial work, complete the adaptive Project Intelligence Gate before
   treating architecture as stable; see `PROJECT_INTELLIGENCE_SOP.md`.
4. Plan and agree scope before material changes.
5. Implement locally, validate proportionately, and inspect the diff.
6. Commit only inside the target repository when requested.
7. Report results, risks, and framework lessons learned.

Global configuration, framework changes, remote actions, deployment, secrets,
and destructive migrations remain explicit approval boundaries.

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
explicit rationale. High-risk scientific, security, or data work uses stronger
gates appropriate to its risk.

The substantial-project flow is an adaptive reference, not a bureaucratic
pipeline. Do not require Terra High, architecture documents, independent
review, or multiple approvals when they do not materially improve the outcome.
