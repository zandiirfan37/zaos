---
name: ml-research
description: "Guide scientifically rigorous tabular predictive-modelling research: formulate the deployment problem, prevent leakage, choose validation from deployment, compare proportionate baselines, and promote only supported evidence. Use for tabular classification or regression research, not generic ML tasks or causal claims."
---

# ML Research

Use this skill for **tabular predictive modelling**. It is project-neutral:
first establish the prediction contract; do not import assumptions from a
project, dataset, or prior experiment.

## Start with the prediction contract

Before selecting a split, feature, or model, state:

1. prediction unit and eligible population;
2. prediction time and information available then;
3. target and its observation horizon;
4. deployment population, cadence, and decision/use case;
5. cost of false positives, false negatives, ranking errors, or probability
   errors.

If these cannot be stated, ask focused questions or label assumptions. Read
[formulation and validation](references/formulation-and-validation.md) before
proceeding.

## Non-negotiable guards

- Make the split boundary before any learned preprocessing, feature selection,
  target encoding, imputation statistic, or tuning. Use pipelines/fold-local
  transformations.
- Reject post-outcome, future, target-proxy, identifier, and cross-split
  leakage. A feature must be reproducible at the prediction time.
- Reserve an untouched final test set where a final unbiased estimate is
  justified; never use it to choose features, models, thresholds, calibration,
  or hyperparameters.
- Choose validation from the deployment process, not habit: IID/stratified,
  grouped, temporal, or rolling/expanding. Read
  [formulation and validation](references/formulation-and-validation.md).

Read [leakage and features](references/leakage-and-features.md) for an audit
or feature design task.

## Research loop

1. Establish a trivial/base-rate baseline, a simple interpretable model, and a
   strong tabular baseline. Complexity must earn incremental value.
2. Engineer only prediction-time-available features: aggregates, trends,
   recency, volatility, interactions, missingness, and categorical handling
   are candidates—not defaults. Keep every learned transform fold-local.
3. Select models proportionately. Linear/logistic models are valid baselines;
   tree ensembles or XGBoost, LightGBM, and CatBoost are candidates when their
   data fit and operational cost justify them. Read
   [models and optimisation](references/models-and-optimisation.md) only when
   choosing or tuning models.
4. Tune against validation only, with an explicit compute budget, seeds,
   tracked configurations, and validation-safe early stopping. Never sweep the
   final test set.
5. Evaluate the decision-aligned metric, calibration when probabilities drive
   decisions, subgroup and temporal robustness, uncertainty where useful, and
   concrete error slices. Read [evaluation and calibration](references/evaluation-and-calibration.md).
6. Consider ensembles only from out-of-fold or otherwise validation-safe
   predictions and only when incremental value exceeds complexity. Use
   explanations for debugging, audit, or decision support—not causal claims.
   Read [evidence and promotion](references/evidence-and-promotion.md) when
   comparing candidates or promoting one.

## Output expectation

Report the prediction contract, split rationale, leakage decisions, baselines,
validation evidence, uncertainty/robustness, and the next decision. Keep it
proportionate: a bounded problem needs a bounded experiment plan.

## Anti-patterns

Do not: random-split by habit; tune on the test set; select features before a
split; use post-outcome data; treat accuracy as universal; sweep blindly;
ensemble automatically; run SHAP automatically; claim prediction establishes
causality; reuse prior-exposed test evidence as final evidence; or choose a
complex model without demonstrated incremental benefit.

## Promotion boundary

`EXPERIMENT → EVIDENCE → DECISION → PROMOTION`.

A winning experiment is not automatically a production model. Promotion needs
the intended deployment contract, reproducible evidence, operational fit, and
an explicit decision owner.

When promotion means picking a winner from many candidates (models,
hyperparameters, or non-tabular candidates such as a hand-crafted scoring
formula) using validation data, read
[candidate selection and stability](references/candidate-selection-and-stability.md)
for resampling-based stability, practical-tie, and freeze-before-confirmation
guidance — it applies beyond tabular modelling and is written domain-neutral.
