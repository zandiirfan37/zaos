# Framework Improvement Loop

Every completed project should report **Framework lessons learned**. Convert
evidence into improvements through this loop:

`project result -> audit -> classify finding -> approved patch or no action`

## Finding classes

- `PROJECT_ONLY_FIX` — correct the current project; no reusable lesson yet.
- `DOCTRINE_PATCH` — update `BIG_SOP.md`, `ENGINEERING_DOCTRINE.md`,
  `PROJECT_INTELLIGENCE_SOP.md`, or another canonical instruction.
- `REFERENCE_EXPANSION` — selectively acquire additional read-only reference
  material under `.agents/reference/` after inventory and approval.
- `ADAPTER_PATCH` — change a Zandi-owned engine adapter or skill.
- `NO_ACTION` — document the finding without changing anything.

Classify each finding by evidence, recurrence, scope, risk, and expected value.
Repo-study and legacy-migration lessons use the same finding classes above;
they do not bypass the evidence or approval requirements.
Architecture lessons may result in `PROJECT_ONLY_FIX`, `DOCTRINE_PATCH`,
`ADAPTER_PATCH`, or `NO_ACTION`, according to that evidence and scope. They do
not make a doctrine change automatic.
Do not turn a one-off project detail into global policy. Require explicit user
approval before changing an adapter or a canonical instruction.
Keep vendored `reference/` material clean and updateable; put local guidance in
Zandi-owned doctrine, not in a vendored tree.

Agents may proactively surface reusable workflow friction—repeated prompt
instructions, a recurring workaround, an avoidable audit, context-loading
inefficiency, or architecture/workflow rework—by routing it through these same
finding classes: a local issue is a `PROJECT_ONLY_FIX`; a reusable pattern is an
`ADAPTER_PATCH` candidate; a systemic or consequential issue goes to
`DOCTRINE_PATCH` review. This is not a new taxonomy—do not recommend a global
change for an isolated project quirk.

When a lesson is accepted, record its evidence, decision, and relevant commit
in the relevant project's durable record. The historical pilot evidence remains
in `archive/VALIDATION_LEDGER.md`; do not turn a one-off lesson into global
policy.
