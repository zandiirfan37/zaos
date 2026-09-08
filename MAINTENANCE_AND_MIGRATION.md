# Maintenance and Migration

How ZAOS doctrine evolves from evidence, and how legacy or external material is
migrated into (or retired from) the active workspace. Low-frequency guidance;
subordinate to `BIG_SOP.md`, never a second authority.

## Framework improvement loop

Every completed project should report **Framework lessons learned**. Convert
evidence into improvements through this loop:

`project result -> audit -> classify finding -> approved patch or no action`

### Finding classes

- `PROJECT_ONLY_FIX` — correct the current project; no reusable lesson yet.
- `DOCTRINE_PATCH` — update `BIG_SOP.md`, `ENGINEERING_DOCTRINE.md`,
  `PROJECT_INTELLIGENCE_SOP.md`, or another canonical instruction.
- `REFERENCE_EXPANSION` — selectively acquire additional read-only reference
  material under `.agents/library/` (curated cards) after inventory and approval.
- `ADAPTER_PATCH` — change a Zandi-owned engine adapter or skill.
- `NO_ACTION` — document the finding without changing anything.

Classify each finding by evidence, recurrence, scope, risk, and expected value.
Repo-study, architecture, and legacy-migration lessons use these same classes;
they do not bypass the evidence or approval requirements, and they do not make a
doctrine change automatic. Do not turn a one-off project detail into global
policy. Require explicit Human Lead approval before changing an adapter or a
canonical instruction.

Agents may proactively surface reusable workflow friction — repeated prompt
instructions, a recurring workaround, an avoidable audit, context-loading
inefficiency, or architecture/workflow rework — by routing it through the same
classes: a local issue is a `PROJECT_ONLY_FIX`; a reusable pattern is an
`ADAPTER_PATCH` candidate; a systemic or consequential issue goes to
`DOCTRINE_PATCH` review. This is not a new taxonomy — do not recommend a global
change for an isolated project quirk.

When a lesson is accepted, record its evidence, decision, and relevant commit in
the owning project's durable record. Historical pilot evidence remains in
`archive/VALIDATION_LEDGER.md`; it is not current operating authority.

## Legacy migration policy

Migrate external legacy material (for example `/home/pc_pusaka/Eksperimen`)
cautiously. Start with a read-only inventory; never move everything at once.
Preserve each legacy project as read-only evidence until its replacement or
parity target is validated. Require explicit Human Lead approval before moving,
deleting, archiving, or rewriting any legacy content. Inventory and decision
evidence must precede each project-by-project action.

### Classification

- `KEEP_AS_ARCHIVE`
- `PATCH_IN_PLACE`
- `REBUILD_CLEAN`
- `MIGRATE_DATA_ONLY`
- `DEPRECATE`

Prefer `REBUILD_CLEAN` when code is messy, dependency-drifted, path-hardcoded,
under-tested, or experimental. A rebuild must define what to preserve and what to
intentionally drop.

### Required artifacts

- `LEGACY_INVENTORY.md`
- `PROJECT_DECISION.md`
- `REBUILD_SPEC.md`
- `PARITY_CHECKLIST.md`
- `MIGRATION_LOG.md`

## The active-workspace archive

Inert, preserved-but-not-active material lives in `/home/pc_pusaka/zandi/.archive/`
(retrieval and provenance storage, never operating authority). Its taxonomy:

- `01_legacy_systems/` — retired frameworks and vendor checkouts (`zaine/`,
  `ecc-zandi-profile/`, `ecc-reference/`).
- `02_closed_pilots/` — completed validation pilots.
- `03_project_history/` — archived predecessors of active projects, with their
  loose migration reports.
- `04_legacy_runtime/` — shadowed pre-cutover engine/config backups.
- `05_personal_archives/` — personal material that was polluting the active tree.

Each archived item keeps its own inner Git history intact. Nothing in the active
control plane, engines, skills, eval, or library depends on an `.archive/` path.

### Retired-framework retrieval notes

Kept only as future references — no resurrection is planned or implied:

- **ZAINE extension governance / project doctor.** If ZAOS ever adds live
  extensions (MCP, hooks, plugins), the capability-manifest + drift model in
  `.archive/01_legacy_systems/zaine/scripts/extension_governance.py` and
  `.archive/01_legacy_systems/zaine/specs/ZAINE_EXTENSION_GOVERNANCE_v1.md` is a
  starting point; the artifact/research contract validators and `project_doctor.py`
  are in the same tree. Promote only against a real consumer, never speculatively.
- **ECC upstream.** `affaan-m/ECC` was pinned at commit `005eff40`
  (`.archive/01_legacy_systems/ecc-reference/`, with its `.git` and
  `ecc.lock.json`). Re-fetch from that provenance if a specific pattern is ever
  needed; it is an idea source, never authority, and is not reinstalled as a
  framework.
