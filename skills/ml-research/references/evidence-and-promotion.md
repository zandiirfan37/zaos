# Evidence, ensembles, explainability, and promotion

- **Topic:** evidence discipline after a valid experiment.
- **Sources:**
  - scikit-learn, [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) and [Inspection](https://scikit-learn.org/stable/inspection.html).
  - MLflow, [ML experiment tracking](https://mlflow.org/docs/latest/ml/tracking/).
- **Why authoritative/useful:** official sources cover held-out evaluation, model inspection tools, and reproducible recording of parameters, metrics, code versions, and artifacts.
- **Accessed:** 2026-09-05.

Ensemble only when validation-safe out-of-fold predictions demonstrate an
incremental improvement that survives uncertainty, robustness checks, and
deployment-cost comparison. Error diversity—not a fashionable model list—is
the reason to combine models. Preserve reproducible constituent models and the
combination rule.

Use coefficient inspection, permutation importance, partial dependence, SHAP,
or local explanations only for a stated purpose: debugging, audit, monitoring,
or human decision support. They describe the fitted predictive relationship;
they do not establish causal effects, fairness, or feature necessity by
themselves.

Track data version/split definition, code revision, feature specification,
seeds, parameters, metrics, artifacts, and decision notes. MLflow is one
possible tracker, not a required dependency.

Promotion requires an explicit chain:

1. **Experiment** — reproducible candidate under a declared split.
2. **Evidence** — comparison, leakage audit, robustness, and uncertainty fit
   the deployment contract.
3. **Decision** — a named owner weighs benefit, risk, calibration, cost, and
   operational feasibility.
4. **Promotion** — only then approve deployment, monitoring, rollback, and
   review expectations.

A prior-exposed test set is historical evidence, not a fresh final gate.
