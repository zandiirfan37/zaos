---
name: testing-strategy
description: Choose the smallest meaningful tests and runtime checks that prove a changed claim, including important failure boundaries. Use when implementation needs verification design; not for executing an entire test suite or replacing project test contracts.
---

# Testing strategy

Start with the claim the change makes and the boundary most likely to regress.
Choose the narrowest combination of deterministic test, integration/smoke path,
or manual observation that can falsify that claim. Include a failure or edge
case only when it distinguishes the behavior; do not add tests that mirror an
implementation detail or repeat a stronger existing check.

Use project-local test contracts and tools. Report an unavailable check and the
residual risk rather than substituting an unrelated green suite. Security,
release, scientific confirmation, and destructive migration assurance remain
HARDENED work, not a testing-strategy decision.
