---
name: code-review
description: Review a material implementation diff against requirements, likely regressions, and adequate verification. Use for risky changes or explicit review; not for routine text or as a substitute for tests.
---

# Code review

Review the actual diff and local authority before trusting a material change.

1. Compare changed behavior to the task and applicable contracts; flag scope drift, missing cases, and authority violations.
2. Follow the changed path far enough to identify likely regressions at callers, error paths, state boundaries, and tests.
3. Check that verification proves the changed claim rather than an adjacent one.
4. Report only actionable findings, ordered by impact, with file evidence; state residual risk when no finding is justified.

Use an independent reviewer or deeper assurance only when the task warrants it. Do not require a second agent, full suite, or release workflow for routine work.
