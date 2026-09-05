---
name: medical-imaging-research
description: "Guide reusable medical-imaging research decisions: data semantics (subjects, orientation/affine, modality), preprocessing/leakage boundaries specific to imaging, exact evaluation-metric contracts (PSNR/SSIM/Dice-style), subject-level validation and external-cohort confirmation, and fair reconstruction/segmentation comparison. Use when designing or auditing a medical-imaging modelling, preprocessing, or evaluation decision. Does not own a project's own formula-specific inverse-problem mathematics — that stays project-local."
---

# Medical Imaging Research

Teaches decision principles for medical-imaging research, not library API usage.
It is domain-neutral within medical imaging: it does not assume a specific
modality, task, or a project's own scientific formula. Read the relevant
section below; read a `references/*` file only for the specific sub-question
it covers.

## Data semantics

Before any preprocessing or modelling decision, establish:

- **Subject/patient identity** and its linkage across every derived file
  (slice, scan, cohort). A subject's data must never be split across
  training/validation/test partitions — this is the imaging-specific form of
  grouped leakage, and it is a stricter rule than a generic row-level split.
- **File-format boundary** (DICOM/NIfTI/HDF5 or another container) and what
  metadata it does and doesn't carry reliably — do not assume header fields
  are populated or consistent across a cohort without checking.
- **Orientation, affine, and spacing** — images from different sources or
  scanners are not guaranteed to share orientation convention, voxel spacing,
  or physical extent; a metric or model that silently assumes a fixed
  orientation/spacing will be systematically wrong on any cohort that
  violates that assumption. State the assumed convention explicitly and
  verify it holds before relying on it.
- **Modality/channel conventions** — which modality or channel a given index
  represents must be an explicit, checked contract, not inferred from file
  order.

## Preprocessing

- **Fit-on-train-only discipline**: any preprocessing step with a learned or
  data-derived parameter (a normalization statistic, a learned atlas/basis,
  an intensity-clipping percentile) must be fit only on the training
  partition and applied without refitting elsewhere — the same rule
  ml-research's leakage guard states for tabular features, applied to
  imaging-specific transforms (intensity normalization, resampling,
  registration/alignment).
- **Cropping/ROI decisions** made at preprocessing time (e.g. restricting to
  a fixed slice range or a bounding region) are themselves a modelling
  choice with scientific consequences — state and freeze the exact rule,
  don't leave it implicit in code.
- **Subject-level leakage** can enter through preprocessing even when the
  split table looks correct: a whole-cohort intensity normalizer, a
  registration atlas built from all subjects, or any transform whose
  parameters were derived before the split existed. Audit the preprocessing
  *pipeline's* data dependencies, not only the final split table.

## Evaluation

Read [metric contracts](references/metric-contracts.md) before freezing an
exact PSNR/SSIM/Dice-style metric definition — the principle, not a specific
project's numbers:

- state data range, evaluated region (whole-image vs. ROI), and
  2D-vs-3D computation explicitly, matched to what the method being
  evaluated actually produces;
- decide subject-level aggregation (mean, median, or a robustness-motivated
  alternative) deliberately, per endpoint, before any outcome is inspected;
- freeze empty-ground-truth and empty/degenerate-prediction handling before
  outcomes are seen — these are common, predictable edge cases in imaging
  data (background-only slices, absent lesions), not rare exceptions;
- keep ROI-restricted metrics secondary to whole-image metrics whenever the
  ROI itself is derived from a label that the primary method must not
  depend on — promoting an ROI metric to primary can silently reintroduce
  the same label-dependence the primary method was designed to avoid.

## Validation

Read [validation and reconstruction fairness](references/validation-and-reconstruction-fairness.md)
for subject-level split design, site/scanner/domain-shift considerations,
and external-cohort confirmation:

- a split is patient/subject-level or it is not a valid split for imaging
  data, regardless of how the row-level table looks;
- external cohort data may confirm a frozen decision; it must never retune
  it — the same freeze-before-confirmation discipline
  `ml-research/references/candidate-selection-and-stability.md` states in
  general, applied to a second/third imaging cohort;
- report subgroup and site/scanner robustness explicitly when the deployment
  or generalization claim depends on it, not only an aggregate metric.

## Reconstruction / segmentation fairness

When comparing multiple reconstruction or segmentation methods:

- enforce a uniform **data-consistency rule** across all methods being
  compared (retained/observed data is never altered by any method; only the
  missing/predicted part is filled) — applying this to only the newer
  methods and not the classical baselines makes the comparison unfair by
  construction;
- record **evaluator/checkpoint provenance** (hash, training-cohort
  boundary) for any learned evaluator or reconstruction model before
  trusting its output as authoritative;
- prefer a **deterministic inference/evaluation contract** for every method
  being compared, including classical/parameter-free ones — determinism is
  cheap to guarantee for classical methods and should not be assumed without
  stating the exact rule (interpolation axis, boundary handling);
- when multiple independent evaluators exist for the same construct (e.g.
  two independently-trained segmentation models scoring the same output),
  averaging them is a defensible way to reduce evaluator-choice leakage;
  choosing the best-looking one after seeing results is not.

## Ecosystem pointers

Use these only as integration references, not as an API tutorial to
reproduce here: **MONAI** and **TorchIO** for imaging-specific transforms
and dataset utilities; **SimpleITK** for orientation/registration/spacing
operations; **pydicom** and **nibabel** for DICOM/NIfTI I/O. Prefer an
established library's implementation over a hand-rolled equivalent for any
of these operations; the scientific decision (which normalization, which
split, which metric contract) still belongs to this skill, not the library.

## Boundary

This skill does not own a project's own formula-specific inverse-problem or
signal-processing mathematics (a custom sampling operator, a spectral
descriptor, a specific basis choice) — that is project-local scientific
work, evidenced and frozen in the project's own state/contracts, not global
methodology. This skill supplies the general medical-imaging data,
preprocessing, evaluation, and validation layer around such project-specific
science, not the science itself.
