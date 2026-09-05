# Validation design and reconstruction/segmentation fairness

## Subject-level splits

A split table that looks correct at the row level can still leak if the
underlying unit is a subject/patient with multiple derived rows (slices,
timepoints, lesions). Verify disjointness at the subject level explicitly —
by set arithmetic over subject identifiers across partitions, not by
inspecting row counts — before trusting any split as leakage-free. This is
the imaging-specific instance of grouped-split discipline; treat it as a
non-negotiable check, not a formality.

## Site/scanner/domain shift

Medical-imaging cohorts frequently differ by acquisition site, scanner
vendor, protocol, or population in ways that change the input distribution
independent of the scientific question being studied. Before claiming a
result generalizes, ask explicitly whether the validation cohort shares
site/scanner/population characteristics with any cohort the result will be
claimed to generalize to. Where it does not, that is exactly the situation
external-cohort confirmation exists to test — do not substitute a same-site
held-out split for a genuine external check when the claim is about
cross-site or cross-scanner generalization.

## External-cohort confirmation

- Confirmation cohorts (a second, third, or later dataset used only to
  check a decision already frozen on a primary cohort) must never be used
  to retune, reselect, or re-derive anything that was supposed to be frozen
  — this is the same freeze-before-confirmation discipline stated in
  `ml-research/references/candidate-selection-and-stability.md`, applied
  here to a second imaging cohort rather than a held-out split of the same
  cohort.
- State explicitly, before a confirmation cohort is opened, what would count
  as the frozen decision being confirmed vs. not confirmed on that cohort —
  deciding this after seeing the confirmation cohort's results defeats the
  purpose of holding it out.
- Report whether a confirmation result preserves the *ranking/ordering* seen
  on the primary cohort, the *absolute magnitude*, or both — these are
  different claims and a manuscript reader will want to know which one is
  being made.

## Subgroup robustness

When a cohort is drawn from structured subgroups (different acquisition
protocols, different severity strata, different demographic groups), report
subgroup-level performance explicitly whenever the deployment or scientific
claim is meant to hold generally across the cohort — an aggregate metric can
hide a subgroup on which the method performs poorly. This is not a
requirement to run every possible subgroup cut; it is a requirement to check
the subgroups that a domain expert would expect to matter for the specific
claim being made.

## Reconstruction/segmentation method fairness

When comparing several reconstruction or segmentation methods (classical
and learned) on the same task:

- **Data consistency**: every method being compared should apply the same
  rule for preserving observed/retained data and only filling in the
  missing/predicted part — apply this uniformly, including to classical
  baselines, not only to learned methods where it is more often stated
  explicitly.
- **Determinism**: classical, parameter-free methods are cheap to make
  fully deterministic (state the exact rule for boundary handling, e.g. at
  the edge of a missing-data run) — do this explicitly rather than assuming
  determinism because the method is simple.
- **Checkpoint/evaluator provenance**: for any learned model or evaluator
  used in the comparison, record which cohort/split it was trained on and
  verify — by checking identifiers, not by assuming — that its training
  data does not overlap with the data it is being evaluated against. A
  reused checkpoint whose training-cohort boundary cannot be verified should
  be treated as needing re-verification or retraining before its outputs
  are trusted as comparable to freshly-trained methods.
- **No outcome leakage into method selection**: none of architecture choice,
  hyperparameters, or checkpoint/epoch selection for a learned method may
  be chosen using the same data that will be used to evaluate the
  comparison's scientific claim — checkpoint selection belongs on a
  validation split, never on the confirmation/test data.
