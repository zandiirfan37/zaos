# ZAOS orchestrator contract

## Architecture locks

Primary human commands are `codex` and `claude`. Scoped shims route only in the configured ZAOS workspace and framework checkout; outside, they execute the preserved vendor command. Flow: native command → workspace/project discovery → task capability → engine adapter → real vendor binary. Raw engines remain reachable. Capability is task/project declared, never implied by launch. Engine differences stay in adapters.

Ordinary maintenance has no outbound-network grant. Remote Git/GitHub work
(`fetch`, `pull`, `push`, remote inspection, sync, and PR operations) requires
the explicit admin route `zaos codex <project> --remote-git` (or `claude`). It
adds outbound access while retaining only the project and resolved Git metadata
scope. Public/external publication is separate and requires
`zaos codex <project> --external-publish`; it is never selected by project name.

When a task needs remote Git/GitHub and `ZAOS_CAPABILITY` is not
`ZAOS_REMOTE_GIT` or `ZAOS_EXTERNAL_PUBLISH`, stop before attempting a remote
operation. Return `CAPABILITY_BLOCKED: ZAOS_REMOTE_GIT`, state that remote
Git/network access is required, and give the exact relaunch command for the
active engine and project. Do not diagnose authentication from a
network/capability-blocked session; report `AUTH_FAILED` only after a
remote-capable session reaches an authentication failure.

## Operating doctrine

Human Lead owns product decisions and `HUMAN_PASS`; the orchestrator owns architecture locks, problem framing, acceptance criteria and decision boundaries; an agent investigates, implements, verifies, and may only declare `ENGINEERING_PASS`. Preflight local authority, workflow, capability, proportional assurance, and material prompt conflict.

Describe failures before prescribing fixes: input → actual behaviour → first wrong layer → expected behaviour → locks. Use smallest healthy vertical slice, engineering evidence, Human Audit early, general root-cause repair, and regression. Workbench is optional only for real uncertainty, destructive rehearsal, parser/security experiments, or benchmarks.

## Boundaries and closure

Agents patch local reversible implementation directly. Stop for a new product decision, architecture/source-of-truth/security-boundary change, irreversible migration, paid action, secret-sensitive decision, or unsupported fact. Meaningful mutation closes with targeted and proportional integration/runtime checks, regression, canonical state update when warranted, commit, and clean worktree. Missing live runtime means `PARTIAL`/`BLOCKED`.

Trace external boundaries: canonical source → build → published artifact → runtime → retrieval/context → model → verifier → renderer. A status code, mock, or readiness endpoint is not end-to-end proof.

## Adoption contract

Tell a friend’s agent: “Clone ZAOS from the canonical repository and install it into my workspace. Follow README exactly. Do not overwrite vendor engines. Run `zaos doctor` and report PASS/BLOCKED.” For updates: “Update ZAOS to the latest compatible canonical version. Run migrations and doctor. Stop on a breaking change or failed verification.”

Detailed doctrine is linked from [instructions/BIG_SOP.md](instructions/BIG_SOP.md); this is the only orchestrator handoff surface.
