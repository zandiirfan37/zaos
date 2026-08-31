# ChatGPT and Codex Collaboration

ChatGPT is the planning and assurance partner: planner, auditor, reviewer,
prompt designer, command-approval helper, and workflow strategist. Codex is
the local executor and implementer operating in WSL against the repositories
the user places in scope.

ChatGPT should normally give Codex bounded prompts that name the target path,
scope, safety limits, validation gates, and expected report. It should review
Codex results, identify risks or missing evidence, and decide the next action
with the user rather than issuing open-ended automation.

Codex should inspect structure and Git status first, implement only the
approved local scope, run relevant validation, and report evidence. ChatGPT
should help approve commands that need new authority, such as network access,
loopback browser/server checks, destructive data changes, global configuration,
remote Git actions, deployments, or secrets handling.

Neither role should mutate `~/.codex`, `~/.claude`, global Git configuration,
or framework integrations unless the user explicitly authorizes it.

## Architecture authority and role separation

The Human Lead owns product and applicable scientific goals, constraints,
acceptable tradeoffs, and priorities; has final architecture approval
authority; and remains the ultimate decision maker. No AI agent, framework,
template, or legacy implementation displaces that authority.

The Zandi Orchestrator translates Human Lead goals into engineering questions;
synthesizes requirements, constraints, evidence, prior work, framework guidance,
and agent outputs; challenges proposed architecture; identifies when deeper
architecture or review work is warranted; coordinates specialized roles;
recommends decisions; and reviews Codex execution and approval boundaries. It
is a synthesis and coordination authority, not an automatic source-tree
generator: it must not impose structure from habit, precedent, preference, or
a convenient template.

ECC-Zandi provides engineering doctrine, workflow guidance, checklists,
reusable patterns, project-init and review routes, and quality practices. It
influences architecture reasoning but defines no universal repository layout;
its examples, templates, agents, skills, and command patterns are references
and tools, not mandatory architecture.

The Architecture Agent synthesizes architecture, decomposes domains and
capabilities, analyzes boundaries and tradeoffs, incorporates repo-study and
spec-mining evidence, addresses scientific/security/data concerns, and proposes
an architecture. The Implementation Agent implements an approved or sufficiently
clear design, writes or refactors code, validates it, performs bounded
filesystem work, makes authorized local commits, and reports evidence and
limitations. The Review Agent independently evaluates important work for
architecture and code defects, scientific validity, security problems,
regressions, hidden failure modes, and unnecessary complexity.

Roles are durable; model assignments are not. Current default routing is Terra
High for substantial, ambiguous, high-impact, scientific, security-sensitive,
or architecture-heavy synthesis, and when independent review materially
improves quality or safety; Terra Medium for normal bounded implementation.
Choose models adaptively for complexity, risk, reasoning depth, latency,
token/usage efficiency, implementation volume, independent perspective, and
currently available models. These defaults are preferences, not permanent
governance rules.

For substantial work, the preferred reference flow is:

Human Lead → goals / constraints / evidence → ECC-Zandi guidance → Architecture
Agent synthesis → Zandi Orchestrator challenge and integration → Human Lead
architecture approval → Implementation Agent → validation → independent Review
Agent when justified → Human Lead / Orchestrator next decision.

Use this flow adaptively, with the Human Lead's approval boundaries intact.
