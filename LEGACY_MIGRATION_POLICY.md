# Legacy Migration Policy

Migrate `/home/pc_pusaka/Eksperimen` cautiously. Start with a read-only
inventory; never move everything at once. Preserve each legacy project as
read-only evidence until its replacement or parity target is validated.

## Classification

- `KEEP_AS_ARCHIVE`
- `PATCH_IN_PLACE`
- `REBUILD_CLEAN`
- `MIGRATE_DATA_ONLY`
- `DEPRECATE`

Prefer `REBUILD_CLEAN` when code is messy, dependency-drifted, path-hardcoded,
under-tested, or experimental. A rebuild must define what to preserve and what
to intentionally drop.

## Required artifacts

- `LEGACY_INVENTORY.md`
- `PROJECT_DECISION.md`
- `REBUILD_SPEC.md`
- `PARITY_CHECKLIST.md`
- `MIGRATION_LOG.md`

Require explicit approval before moving, deleting, archiving, or rewriting any
legacy project content. Inventory and decision evidence must precede each
project-by-project migration action.
