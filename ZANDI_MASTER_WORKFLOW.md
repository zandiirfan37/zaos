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
3. Plan and agree scope before material changes.
4. Implement locally, validate proportionately, and inspect the diff.
5. Commit only inside the target repository when requested.
6. Report results, risks, and framework lessons learned.

Global configuration, framework changes, remote actions, deployment, secrets,
and destructive migrations remain explicit approval boundaries.
