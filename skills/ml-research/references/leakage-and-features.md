# Leakage and feature engineering

- **Topic:** point-in-time feature safety and fold-local transformations.
- **Sources:** scikit-learn, [Common pitfalls: data leakage](https://scikit-learn.org/stable/common_pitfalls.html) and [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html).
- **Why authoritative/useful:** official documentation defines leakage as information unavailable at prediction time and demonstrates train-only fitting and pipeline isolation.
- **Accessed:** 2026-09-05.

## Leakage audit

For every feature, record source timestamp, availability timestamp, aggregation
window, target relationship, and whether its transformation is fit only inside
each training fold. Reject or isolate:

- post-outcome fields, later status, resolution, or intervention data;
- future information in aggregates, joins, rolling windows, or label delay;
- target proxies and leakage-prone IDs that encode the outcome process;
- identifiers that cause memorisation rather than deployable signal;
- preprocessing, imputation, scaling, encoding, feature selection, or target
  encoding fit before splitting;
- rows, entities, or duplicate records crossing a split boundary.

## Safe feature candidates

Subject to the audit, consider prediction-time aggregates, trend/slope,
recency, volatility, counts/rates with correctly closed windows, missingness
indicators, and domain-justified interactions. Categorical handling must be
fit fold-locally; target-informed encodings require especially careful
out-of-fold construction.

Use a pipeline or equivalent fold-local process so every learned transform fits
on training data and only transforms validation/test data. A useful general
rule: a deployment-time cohort/group variable may be reserved for splitting or
audit rather than used as a predictor when using it would defeat the intended
generalisation test.
