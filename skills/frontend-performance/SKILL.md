---
name: frontend-performance
description: Improve or review React/Next.js performance at an observed or plausible rendering, data-fetch, bundle, or interaction bottleneck. Use for frontend performance work; not for visual design, generic backend tuning, or speculative micro-optimization.
---

# Frontend performance

First identify the user-visible or measured bottleneck and its boundary. Prefer
high-impact causes before micro-optimizations: sequential independent async
work, unnecessary client payload, duplicate fetch/serialization, avoidable
rerenders, and costly rendering of long or hidden content. Preserve semantics,
accessibility, error states, and project data/cache contracts.

Measure or inspect the changed path enough to support the claim. Do not add
memoization, caching, dynamic imports, or a dependency merely by pattern;
explain the cost it removes and verify the closest failure/loading path. Pair
with UI/UX Pro Max only when the task also changes visual or interaction design.
