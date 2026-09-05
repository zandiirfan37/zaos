# Candidate/model selection under resampling — domain-agnostic

Read this when a task needs to pick a winner among many candidates (models,
hyperparameters, hand-crafted formulas, thresholds, configurations) using a
validation set, and wants to know whether the winner is real or noise. This
applies whether "candidate" means a tabular model, a descriptor formula, a
threshold rule, or any other scored object — the methodology below depends
only on the selection procedure's statistical shape, not on the domain of
what is being selected.

## Selection vs. estimation

Choosing a winner from a candidate set on the same data used to score that
set conflates *selection* with *estimation*: the winning score is an
optimistic estimate of that candidate's true performance, even when a
further held-out/external set remains genuinely untouched. Name this
plainly wherever it applies — do not call a fixed-partition, same-data
selection procedure "cross-validation" as if it estimated generalization
error; it estimates *which candidate wins on this data*, which is a
different and narrower claim.

## Resampling design

- **Resampling unit** = the level at which observations are naturally
  correlated (a subject, a patient, a time series, a cluster) — never the
  raw row level when rows share that unit. Resample *with replacement* at
  that unit, and carry every row belonging to a resampled unit together;
  splitting a unit's rows across resample draws breaks the exchangeability
  the method relies on.
- **Full-registry vs. shortlisted bootstrap**: score every eligible
  candidate per resample when scoring is cheap (closed-form, no retraining)
  — this is usually the *simpler*, more defensible choice, since a
  shortlist cutoff needs its own justification (which K, chosen how). Fall
  back to a shortlist only when scoring itself is expensive (e.g. each
  candidate requires retraining a model), and say explicitly why the
  shortlist was chosen and how.
- **Replicate count**: enough for stable percentile estimates of the
  quantities below; there is no universal number — pick one and state the
  precision it buys (e.g., the resulting Monte Carlo error on a percentile
  bound), rather than citing a replicate count as an authority in itself.

## What to report from the resampling

- **Winner frequency** — how often each candidate is the arg-max across
  resamples. A point-estimate winner that wins rarely under resampling is a
  fragile winner, whatever its single-sample score.
- **Rank/weight stability** — whether the winner's neighbourhood (similar
  candidates, similar configurations) stays similar across resamples, not
  just whether the exact winner repeats.
- **Paired bootstrap uncertainty** — when comparing two specific candidates,
  use the resampled *difference* between their scores per replicate, not
  each candidate's marginal resampled distribution independently; a paired
  comparison correctly accounts for their shared resampling and is usually
  tighter and more honest than comparing two marginal intervals.

## The resampling result is a stability report, not a second objective

State this boundary explicitly wherever the pattern is used: the winner is
still whichever candidate maximizes the primary objective on the real,
non-resampled data. The resampling characterizes how much to trust that
winner — it does not silently re-rank candidates, and it must never become
an unregistered second selection criterion applied after the fact.

## Practical equivalence ("ties")

Exact numerical equality between candidate scores is not a realistic
criterion. Define "practically tied" using the resampling uncertainty
itself — for example, two candidates are tied if their resampled score
difference's standard error comfortably contains zero — rather than
inventing an arbitrary fixed epsilon with no statistical grounding. When
candidates are tied under this rule, fall through to a pre-registered
deterministic tie-breaker (a fixed priority order decided before any
outcome was seen), not a fresh judgment call made after seeing the numbers.

## Multiplicity without pretending independence

Many correlated candidates (linear combinations of a small number of
underlying components, neighbouring hyperparameter values, near-duplicate
configurations) are not the same thing as many independent hypotheses.
Applying a family-wise or false-discovery-rate correction designed for
independent tests (as in a many-exposure screening study) to a smooth,
structured candidate space is a category error — it corrects for a
multiplicity that does not exist in that shape. For an arg-max-over-a-
structured-space problem, the resampling-based stability report above is
the right tool; for a genuine many-independent-hypotheses screen, use an
FWER/FDR correction instead. Know which shape the problem actually has
before choosing the tool, and say which one you used and why.

Before trusting a large candidate registry's size at face value, check
whether its components are actually independent contributors to the score
or whether some are empirically near-duplicates of others (a simple
pairwise correlation check across representative cases is usually enough).
A registry of size N with highly correlated components has fewer effective
degrees of freedom than N — report this rather than letting nominal
candidate count imply a false precision.

## Robustness gates

A single scalar objective can be maximized by a candidate that is excellent
on most of what it's evaluated against and merely non-negative on the rest
— equal-weight averaging does not by itself guard against this. Prefer a
gate with a principled, pre-specified threshold over a scalar-only
objective: for example, require a resampled lower confidence bound on each
material sub-group's (method's, endpoint's, condition's) association to
clear a null-referenced floor (e.g., greater than the value that would mean
"no better than chance"), rather than picking a threshold value with no
stated rationale. Make the gate's pass/fail condition an explicit,
pre-registered requirement for using the candidate, not an optional
diagnostic read after the fact.

## Degenerate and missing data

Freeze, before any real outcome is inspected, what happens when a cell of
the evaluation (a partition/group/condition combination) has too little
data, zero or near-zero variance, or a non-finite value: whether it is
excluded from the aggregate (and logged, never silently imputed), and what
minimum fraction of cells must remain valid before the aggregate is still
trusted. Deciding this rule after seeing which cells are inconvenient is
exactly the kind of post-hoc choice that undermines the whole exercise.

## Freeze before confirmation

Once a winner is chosen and its resampling-based stability characterized,
freeze the winning candidate, its selection procedure, and any derived
rule (a threshold, a decision boundary) that depends only on the
already-inspected validation data — before opening any further held-out or
external data. External/held-out data may *confirm* the frozen choice; it
must never be used to retune, re-select, or re-derive anything that was
supposed to be frozen. If a derived rule (like a threshold) needs to exist
at all, its exact derivation method must be decided and frozen at the same
time as the candidate itself — not chosen once the validation score
distribution is visible, which would be a hidden second tuning step.
