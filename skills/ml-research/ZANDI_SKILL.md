# Zandi skill metadata — ML Research

- **Name:** ml-research
- **Category:** DOMAIN
- **Owner:** Zandi
- **Status:** TESTED
- **Created:** 2026-09-05
- **Scope:** scientifically rigorous tabular predictive modelling: formulation, leakage, deployment-aligned validation, baselines, feature engineering, model selection, tuning, evaluation, calibration, ensembles, explainability, and promotion.
- **Sources:** official scikit-learn, XGBoost, LightGBM, CatBoost, Optuna, and MLflow documentation; Cerqueira, Torgo, and Mozetic (2019) for temporally ordered performance estimation.
- **Tested scenarios:** A passed — IID churn chose repeated stratified validation; B passed — future-cohort deployment chose chronological/expanding validation; C passed — unsafe all-columns/XGBoost/accuracy request was challenged for prediction contract, leakage, split, baselines, and task-aligned metrics.
- **Known limitations:** not a causal-inference, deep-learning, NLP, computer-vision, or production-operations playbook; it cannot infer an unavailable deployment contract.
- **Change history:** v0.1 created 2026-09-05; promoted from DRAFT to TESTED on 2026-09-05 after three bounded behavioral tests. TRUSTED requires real-project use.
