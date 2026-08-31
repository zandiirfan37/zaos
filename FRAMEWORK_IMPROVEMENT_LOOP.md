# Framework Improvement Loop

Every completed project should report **Framework lessons learned**. Convert
evidence into improvements through this loop:

`project result -> audit -> classify finding -> approved patch or no action`

## Finding classes

- `PROJECT_ONLY_FIX` — correct the current project; no reusable lesson yet.
- `PROFILE_PATCH` — improve a controlled project-use profile, such as
  ECC-Zandi guidance.
- `UPSTREAM_COMPONENT_EXPANSION` — selectively acquire additional upstream
  reference material after inventory and approval.
- `FRAMEWORK_ADAPTER_PATCH` — change a Zandi-owned adapter or wrapper.
- `GLOBAL_INSTRUCTION_PATCH` — update these workspace-wide instructions.
- `NO_ACTION` — document the finding without changing anything.

Classify each finding by evidence, recurrence, scope, risk, and expected value.
Repo-study and legacy-migration lessons use the same six finding classes above;
they do not bypass the evidence or approval requirements.
Architecture lessons may therefore result in `PROJECT_ONLY_FIX`, `PROFILE_PATCH`,
`GLOBAL_INSTRUCTION_PATCH`, or `NO_ACTION`, according to that evidence and
scope. They do not make a framework or global change automatic.
Do not turn a one-off project detail into global policy. Require explicit user
approval before changing a framework, profile, adapter, or global instruction.
Keep upstream repositories clean and updateable; prefer Zandi-owned adapters
for local guidance changes.

When a lesson is accepted, record its evidence, decision, and relevant commit
in `VALIDATION_LEDGER.md` so future sessions can distinguish validated practice
from a proposal.
