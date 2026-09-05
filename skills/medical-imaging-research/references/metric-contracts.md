# Metric contracts for medical-imaging evaluation

Freeze an exact definition before computing any metric below — a metric
"name" (PSNR, SSIM, Dice) is not a contract until every one of these choices
is stated. This file teaches the decision principles; a project's own chosen
values (its data range, its exact aggregation statistic, its threshold) are
project-local and belong in that project's own frozen contract, not here.

## PSNR

- **Data range** must match the actual normalization/clipping convention
  applied to the images being compared — a floating, per-image data range
  makes PSNR values incomparable across cases; a single frozen constant
  (derived from the pipeline's own normalization contract) is required for
  comparability.
- **Evaluated region**: decide deliberately whether "whole image" includes
  background/non-tissue voxels. Including them is defensible when the
  evaluation's purpose is relative (comparing methods/scenarios against each
  other, since background affects all methods similarly) but will compress
  and inflate the absolute numbers reported — disclose this rather than
  silently restricting to a tissue mask not present in the frozen
  preprocessing contract.
- **2D vs. 3D / per-slice vs. volumetric**: match the evaluation's grain to
  what the method under test actually operates on. Evaluating per-slice and
  aggregating is more diagnostic (it does not let strong slices hide
  localized failure) than a single volumetric number, when the method itself
  operates slice-wise; match a volumetric method with volumetric evaluation.
- **Degenerate/constant-array handling**: a slice that is byte-identical
  between prediction and ground truth (e.g. a pure-background slice)
  produces an infinite PSNR under the standard formula. Freeze a finite
  ceiling to clip to (rather than propagating infinity into any downstream
  aggregate) and log how often it triggers as a QA diagnostic — do not treat
  a triggered ceiling as a silent, unremarkable event.

## SSIM

- Same data-range and region-matching decisions as PSNR, and they should be
  kept consistent between the two metrics when both are reported for the
  same comparison.
- **Windowing**: a windowed (typically Gaussian-weighted) local-statistics
  computation is the standard construction; state the window definition
  used, since SSIM is more sensitive to this choice than PSNR is to its
  analogous choices.
- **Near-constant-region failure mode**: SSIM's local-variance term becomes
  numerically defined but scientifically uninformative on a near-constant
  patch (e.g. background), typically saturating near its maximum trivially.
  Decide and freeze a rule (e.g. excluding patches/slices below a variance
  floor from the aggregate, with the exclusion count logged) rather than
  silently averaging in values that compress the real differences between
  methods.
- **True 3D SSIM** (windowing across slices, not just in-plane) is only
  appropriate when the method being evaluated actually uses cross-slice
  information in producing its output; applying 3D windowing to a method
  that operates slice-independently evaluates information the method never
  had, which can misattribute quality to structure the method didn't
  produce.

## Segmentation overlap (Dice-style)

- **Prediction threshold/binarization** must be a frozen, deterministic rule
  (e.g. a fixed probability cutoff), decided before any output is scored,
  not chosen post hoc to make numbers look better.
- **Empty-ground-truth and empty-prediction handling** are both common,
  predictable cases in imaging data (an absent lesion, a missed detection)
  and must have a frozen convention *before* outcomes are seen — for
  example, treating both-empty as perfect agreement and one-empty as zero
  agreement is a common, defensible convention, but whatever convention is
  chosen must be stated, not left to whatever the implementation happens to
  do by default (many implementations silently produce NaN or divide-by-zero
  here).
- **Multiple independent evaluators**: when more than one independently
  produced segmentation/scoring model exists for the same construct,
  combining them (e.g. by averaging) before or instead of picking "the
  better one" removes an entire leakage vector — post-hoc evaluator
  selection based on which one supports the desired result is exactly the
  kind of choice that must be frozen in advance, not made after seeing
  outcomes.
- A standard overlap-based formula already penalizes gross over- or
  under-segmentation through its own denominator; do not add an ad hoc
  correction for a pathological prediction unless a genuine numerical
  failure mode (not just a low score) is identified.

## Subject-level aggregation

Decide the statistic used to combine per-case values into one value per
group (per scenario, per condition, per fold) deliberately, and consider
that different endpoints may warrant different choices:

- a small group size makes a plain mean sensitive to a single outlier case
  (e.g. one catastrophic reconstruction failure) — a robustified statistic
  (a trimmed mean, or median for a genuinely bounded/tie-heavy endpoint) is
  often more defensible than an unweighted mean, but state which was chosen
  and why for each endpoint rather than assuming one rule fits all metrics.
- prefer a single, simply-stated rule across endpoints when a robustified
  option resolves every endpoint's specific concern, rather than inventing a
  different rule per endpoint merely because their raw behavior differs —
  simplicity that is provably sufficient beats a bespoke rule per metric.

## ROI vs. whole-image metrics

Restricting a metric to a region of interest is legitimate for interpreting
quality specifically inside that region, but if the ROI itself is derived
from a label the primary method is not supposed to depend on (e.g. a lesion
mask), promoting the ROI metric to a *primary* evaluation criterion can
silently reintroduce that label-dependence into the primary claim. Keep such
metrics secondary/diagnostic unless the primary method's own contract
already permits label access.
