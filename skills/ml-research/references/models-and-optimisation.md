# Models and optimisation

- **Topic:** proportionate tabular baselines, validation-safe boosting, and bounded HPO.
- **Sources:**
  - scikit-learn, [Model selection and evaluation](https://scikit-learn.org/stable/model_selection).
  - XGBoost, [Python training / early stopping](https://xgboost.readthedocs.io/en/stable/python/python_api.html).
  - LightGBM, [Python introduction / early stopping](https://lightgbm.readthedocs.io/en/stable/Python-Intro.html).
  - CatBoost, [parameter tuning](https://catboost.ai/docs/en/concepts/parameter-tuning) and [categorical features](https://catboost.ai/docs/en/features/categorical-features).
  - Optuna, [efficient optimisation algorithms](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/003_efficient_optimization_algorithms.html).
- **Why authoritative/useful:** these are official implementation references for model-family behaviour, early stopping, categorical treatment, and trial pruning.
- **Accessed:** 2026-09-05.

## Candidate ladder

Begin with a dummy/base-rate comparator, then a simple interpretable model
(linear/logistic or regularised variant), then a strong tabular baseline such as
histogram gradient boosting. Compare XGBoost, LightGBM, or CatBoost only when
their expected value justifies added dependencies and operational complexity.
CatBoost can be a useful categorical-feature candidate; do not pre-encode by
habit or assume any booster is universally best.

## Tuning rules

Fix the split design first. Define primary validation metric, secondary safety
metrics, compute/time budget, seed policy, and stopping criterion. Tune only on
training/validation folds; record the search space and every result. Use a
separate validation fold or fold-local CV for early stopping—never the final
test. Optuna pruning can save compute on unpromising trials but does not make
an invalid validation design valid.

Stop when gains are within uncertainty, operational cost outweighs them, or the
baseline is adequate. Refit only according to a predeclared plan after model
selection; preserve the untouched test for its intended one-time evaluation.
