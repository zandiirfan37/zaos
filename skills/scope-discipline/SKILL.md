---
name: scope-discipline
description: Keep a change proportionate when abstraction, dependencies, services, rewrites, or cleanup begin expanding beyond the requested outcome. Use for anti-overengineering review; not to block evidence-backed necessary complexity.
---

# Scope discipline

Use this only when scope is growing. Restate the concrete outcome and smallest change that delivers it. For each proposed abstraction, dependency, service, or adjacent refactor, name the present failure or repeated consumer it solves; otherwise defer it.

Prefer an existing local pattern and reversible implementation. Preserve valid work; do not bundle cleanup merely because files are nearby. If the minimal solution would knowingly violate an authority, reliability boundary, or future cost already evidenced, explain that constraint and choose the smallest safe alternative.

Escalate once only when the remaining choice is genuinely consequential. This skill does not create a permission gate for routine work.
