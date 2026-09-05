# Formulation and validation

- **Topic:** prediction contracts and deployment-aligned validation.
- **Sources:**
  - scikit-learn, [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) and [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html).
  - Cerqueira, Torgo & Mozetic, [Evaluating time series forecasting models](https://arxiv.org/abs/1905.11744), 2019.
- **Why authoritative/useful:** scikit-learn documents the operational splitters; the peer-reviewed empirical study examines performance estimation under temporal non-stationarity.
- **Accessed:** 2026-09-05.

## Decision rule

Validation estimates the deployment question. Write the prediction time,
training cutoff, scoring horizon, entity relationship, and target availability
before naming a splitter.

| Deployment condition | Appropriate starting design |
| --- | --- |
| New examples are exchangeable with training examples | repeated IID CV; stratify classification when class balance matters. |
| Entities recur and deployment is to unseen entities | grouped CV; consider stratified-group splitting if both constraints matter. |
| Predictions are made for later periods/cohorts, or drift/future availability is plausible | chronological holdout plus forward/rolling or expanding-origin validation. |
| Both time and repeated entities matter | preserve chronology and prevent entity leakage; design custom folds if needed. |

TimeSeriesSplit is an expanding-window tool for ordered, suitably spaced data;
its `gap`, test horizon, and maximum train size must represent the deployment
delay and history policy. Do not use it mechanically for arbitrary cohorts.

Reserve an untouched test only if enough data exists and a final decision needs
a one-time unbiased estimate. Model selection, threshold choice, calibration,
and feature design use training/validation folds. Nested validation is useful
when the selection process itself needs an unbiased performance estimate; it is
not ceremony for every bounded experiment.

Temporal validation is preferred when future deployment is the estimand. Random
splits may be a supporting diagnostic only after evidence supports temporal
exchangeability and feature availability is point-in-time safe.
