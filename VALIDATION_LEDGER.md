# Zandi Validation Ledger

This ledger records accepted Zandi operating evidence, not a substitute for
checking current repository status before a new task.

## Completed milestones

- Umbrella migration completed; Zandi root intentionally remains non-Git.
- ECC acquired as a partial sparse upstream repository at commit
  `005eff40fd4a4ac005da7a70e713459175385516`.
- ECC-Zandi profile created, then relocated under the ECC framework group
  (`b036d85e8919c4a732327b1182713eb83095d1f8`).
- Zandi MiniLab pilot built and committed locally (`9ffe7ef292c21772bf60f0057149818deb632d0a`),
  with local environment hygiene follow-up (`415793200f35b6822396d0d1d96fd78f0b075e15`).
- Terra High audits identified SQLite lifecycle, route-coverage, input-bound,
  and test-fixture lessons.
- MiniLab hardening applied (`f744b75fb2f8c84add7bcd0701f4f66e2ad235c3` and
  `093976baa71a04555a20106ec9ffc14fe068f3ee`), followed by strengthened route
  and bounds coverage (`9ed8e9581ccc0be7e0d0839239af8acad4f54f14`).
- ECC-Zandi profile received the accepted MiniLab web-app quality lessons
  (`c3df989f687e65e3b80619a8214a895d4a513608`).
- Starter-pack, cleanroom-study, and legacy-migration policies established in
  the Zandi instructions repository.
- GradTime clean-slate rebuild validated a general lesson: preserve legitimate
  requirements, behavior, semantics, evidence, provenance, and parity needs;
  independently synthesize the replacement architecture.
- GradTime surfaced a second governance failure class: the R9 feature-family
  tournament was frozen inside an already-narrowed IPS/SKS candidate set, and
  the omitted original field `JENJANG` (degree level) later produced a large
  improvement at R11B. The clean rebuild had also declared its experimental
  scope complete without a systematic legacy design-intelligence recovery
  pass. Governance patched (ECC-Zandi `c15c592`; instructions, this commit):
  `PROJECT_INTELLIGENCE_SOP.md` gains a Canonical Intelligence Memory model, a
  Legacy Design-Intelligence Recovery Gate (F), a Resource / Feature Universe
  Gate (G), a strengthened Reference Design synthesis requirement, and a
  Study-Design Freeze Gate (H); `EFFICIENT_AGENTIC_ENGINEERING.md` gains
  feature-universe completeness in the feature-engineering gate plus matching
  anti-patterns; `ZANDI_MASTER_WORKFLOW.md` defines the design-collaborator
  completion envelope and reaffirms Fast Lane preservation;
  `MULTI_AGENT_ROUTING.md` clarifies the design-collaborator role. GradTime
  implementation unchanged (read-only failure evidence).
- GradTime intelligence-to-blueprint replay closed three remaining
  operating-model gaps with a bounded governance patch (ECC-Zandi `5d7d9f9`;
  instructions, this commit): `PROJECT_INTELLIGENCE_SOP.md` gains a
  "Focused high-intelligence passes" doctrine (separate bounded High passes for
  legacy / reference / data / domain / synthesis, returning to Medium after
  blueprint freeze), Section B dataset- and variable-level depth requirements
  plus an optional machine-readable resource registry and preprocessing
  discipline (no unevidenced MCAR/MAR/MNAR, no blind global imputation of
  structural missingness, learned preprocessing fit on the training partition
  only), and a Blueprint Synthesis Gate (Section I) with `INTELLIGENCE_COMPLETE`
  / `BLUEPRINT_SYNTHESIS_REQUIRED` / `BLUEPRINT_READY_FOR_IMPLEMENTATION` freeze
  outputs and a post-freeze Medium stage-execution loop;
  `ZANDI_MASTER_WORKFLOW.md` adds blueprint convergence to the
  substantial-project flow, the post-freeze Medium stage-execution model, and
  keeps Fast Lane exempt; `MULTI_AGENT_ROUTING.md` states the High/Medium
  economic intent; `EFFICIENT_AGENTIC_ENGINEERING.md` gains a "Data
  intelligence depth and preprocessing discipline" doctrine plus matching
  anti-patterns. GradTime implementation unchanged (read-only replay).
- `GOVERNANCE_FREEZE` re-affirmed after this patch: no further Zandi governance
  change without another concrete project failure. No speculative audit loop.

## What MiniLab validated

The pilot validated the ECC-Zandi loop across planning, architecture,
implementation, SQLite persistence, FastAPI, unit/persistence tests, browser
smoke, real loopback route integration, hardening, audit, and profile feedback.

## Known limitations

MiniLab remains local-only: no authentication, CSRF protection, deployment, or
remote. Loopback permission may be needed in restricted environments for route
integration tests. These are deliberate pilot boundaries, not evidence that
shared or deployed apps are ready.

Every future project report must include **Framework lessons learned** and use
the improvement loop to classify whether a finding needs a project fix, profile
patch, framework change, global instruction patch, or no action.
