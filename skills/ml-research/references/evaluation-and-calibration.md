# Evaluation and calibration

- **Topic:** task-aligned metrics, probability calibration, robustness, and uncertainty.
- **Sources:**
  - scikit-learn, [Model selection and evaluation](https://scikit-learn.org/stable/model_selection) and [Probability calibration](https://scikit-learn.org/stable/modules/calibration.html).
  - Van Calster et al., [Calibrating machine learning approaches for probability estimation](https://pubmed.ncbi.nlm.nih.gov/37849356/), *Statistics in Medicine*, 2023.
- **Why authoritative/useful:** scikit-learn documents cross-validated calibration; the peer-reviewed comparison evaluates common calibration approaches and external-population concerns.
- **Accessed:** 2026-09-05.

Discrimination answers whether positives tend to rank above negatives;
calibration answers whether predicted probabilities match observed frequencies.
Neither makes accuracy a universal metric.

Choose metrics from the decision: e.g. MAE/RMSE for regression error,
log-loss/Brier score for probability quality, PR-AUC for rare-positive ranking,
ROC-AUC for ranking across thresholds, and thresholded utility/recall/precision
only with an explicit operating point. Report prevalence and a trivial baseline.

When probabilities drive decisions, inspect calibration curves and proper scores
on validation data. Fit a calibrator on data independent of base-model fitting:
use out-of-fold predictions or a separate calibration split. Choose sigmoid,
isotonic, or another method empirically with adequate sample support; do not
assume calibration improves every model or extrapolates to a shifted population.

Inspect temporal/cohort and decision-relevant subgroup performance with enough
sample/event counts. Report fold variation, bootstrap or other uncertainty
intervals when they can change the decision. Perform error analysis on concrete
failure slices; avoid reading importance or calibration as causal evidence.
