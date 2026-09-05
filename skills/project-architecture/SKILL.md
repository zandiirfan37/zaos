---
name: project-architecture
description: Derive the minimum professional, domain-specific project architecture from actual execution, data, risk, and reproducibility needs. Use when a project's structure/boundaries need to be derived or materially reconsidered, or when a clean project needs to be stood up early during recovery/rebuild. Not a universal folder template.
---

# Project Architecture

Narrow, reusable, on-demand architecture-derivation skill. It is not a folder
template, not a parallel project-management framework, and not a replacement
for `project-refoundation`, which owns recovery/rebuild orchestration and calls
into this skill at its convergence step. No concept below automatically implies
a folder — create only what a real, current need justifies. Complexity must
pay rent.

## Core loop

```
UNDERSTAND GOAL
→ IDENTIFY EXECUTION / DATA / RISK / REPRODUCIBILITY NEEDS
→ DERIVE MINIMUM CONCEPTUAL BOUNDARIES
→ EXPLAIN MATERIAL CHOICES
→ HUMAN/ORCHESTRATOR APPROVAL IF CONSEQUENTIAL
→ CREATE ONLY JUSTIFIED STRUCTURE
→ RE-DERIVE LATER ONLY WHEN MATERIAL EVIDENCE CHANGES NEEDS
```

Reason in concepts before physical directories. Potential concepts, each
justified independently, never bundled by reflex:

- local authority/current state
- executable source
- environment/dependencies
- tests/verification
- configuration/contracts
- external resources/data
- experiments/workbench
- notebooks
- generated artifacts/runs
- lineage
- domain modules
- release/serving boundaries

A tiny utility may need only executable code, a dependency declaration if one
is needed, focused verification, and concise instructions. Do not create
src/config/data/notebooks/artifacts/workbench trees by reflex for small work.

## Early clean home

For `REBUILD_CLEAN`, `HYBRID_REBUILD`, or similar cases where a new home is
needed, create the clean project **early**, once:

1. a recovery/build mode is chosen;
2. material legacy findings have enough disposition to know what must not be
   repeated and what is worth preserving;
3. a minimum executable boundary is nameable.

Do not wait by default for complete reference intelligence, complete data
intelligence, a final architecture, or a giant blueprint — those continue
inside the clean project. Do not create speculative empty scaffolding before
triage can even name the mode and minimum boundary — that is the opposite
failure.

`project-refoundation` references this rule rather than duplicating it.

## Professional reference timing

Default: a minimum clean architecture may exist first; references then refine
it incrementally. `LEARN_ONLY` / `BORROW_PATTERN` / `ADOPT_COMPONENT` should
normally not block creating the minimal clean project.

Exception: if `MAJOR_ADOPTION` or `USE_AS_BASE` is a realistic candidate, make
that reference decision *before* committing heavily to a custom architecture —
you may adopt the reference's shape instead of building your own.

## Numbering / ordered research

Number where order materially aids navigation. Use semantic names where
identity matters more than sequence.

Number by default: ordered research stages, experiment directories, sequential
study/run scripts, experiment configs, evidence/reports, migration stages,
ordered notebooks when a real order exists. Example:

```
01_vis/
02_baselines/
03_resnet/
```

Parallel branches share a stable suffix rather than consuming a new sequence
number:

```
03a_resnet
03b_resnet_aug
```

Do not renumber historical stages merely because research evolves — record
status instead (`ACTIVE` / `SUPERSEDED` / `PARALLEL`, plus the parent or
superseding unit when material) in `PROJECT_STATE.md` or an existing compact
local artifact. Do not create a new lineage framework.

Never number by default: Python package/domain modules, reusable libraries,
canonical APIs, standard or tool-required files (`pyproject.toml`,
`AGENTS.md`, `PROJECT_STATE.md`, `README.md`, `__init__.py`, ...). Numbers
represent navigation/research order, not a claim of strict causal or
execution order.

## Freeze / evidence-promotion pattern

When a research project starts producing exploratory work, evidence, and
consequential scientific decisions, a recognizable separation recurs across
unrelated Zandi projects independently:

```
WORKBENCH / EXPLORATION
→ EVIDENCE
→ DECISION GATE
→ FROZEN/CANONICAL CONTRACT (+ provenance/hash)
→ HARDEN / RELEASE / CONTINUE
```

Exploratory work stays cheap and reversible; only evidence that survives a
decision gate is promoted; a frozen contract records what was decided, with
enough provenance (a hash, a pointer, a version) to know exactly what was
frozen and why. This is a pattern to **recognize and offer** when a
project's own state shows the need emerging — not a mandatory template, not
a folder structure to impose in advance, and not a reason to invent stage
numbering or freeze infrastructure for a small project that has no
consequential decision to protect yet. Use whatever terminology the project
already has for these roles rather than renaming an existing convention to
match this list.

## Data architecture

Separate three distinct decisions:

1. **Canonical ownership / target layout** — cheap, reversible; decide early.
2. **Manifest / config / path contract** — cheap, additive; create early,
   right after (1).
3. **Physical data movement** — expensive, risky; do not move large datasets
   merely for cleanliness. Move only once a concrete trigger exists (legacy
   location unstable, shared, or about to disappear; or derived-data
   generation must start) and migration impact is understood.

Before material physical migration, consider provenance, file counts/hashes,
schema checks, path dependencies, split/identity linkage, rollback, storage
duplication, and shared reuse across projects. Keep raw/source data
immutable by default. Derived data, metadata, QC, manifests, splits, caches,
and generated outputs are distinct concepts only when they actually exist and
matter for the project at hand.

## Boundaries

Re-derive architecture only when material evidence changes the current needs
— not on a schedule, and not because a reference or dataset was merely
inspected. Record durable architecture decisions in project-local
`PROJECT_STATE.md` / `AGENTS.md`, not in this skill. Escalate to the Human
Lead (directly, or via Council when the choice is genuinely ambiguous) before
a consequential, hard-to-reverse structural or data-migration decision.
