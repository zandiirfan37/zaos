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
- **Change history:** v0.1 created 2026-09-05; promoted from DRAFT to TESTED on 2026-09-05 after three bounded behavioral tests. v0.2 (2026-09-05): added `references/candidate-selection-and-stability.md` (domain-agnostic resampling-based candidate/model-selection methodology, cross-referenced at the promotion-boundary step) and one cross-reference sentence in `SKILL.md`; scope/frontmatter unchanged, still tabular-only for the skill's own identity. Status unchanged (TESTED); this was an additive patch, not a scope broadening. TRUSTED requires real-project use.
- **Eval (2026-09-06):** first skill evaluated by the ZAOS harness (`.agents/eval/`). `eval/cases.toml` = 5 behavioural + 1 static + 1 activation, each with regression tripwires. Results: `sonnet` floor **7/7 PASS** (`.runtime/eval/ml-research/PILOT-v2`, $0.35). `haiku --ab` **skill lift on 2/3** cases (`HAIKU-AB`). Regression check: a deliberately-weakened copy (guards removed, "use a random split" injected) **fails 2/3 on `haiku`** (`HAIKU-REGRESSED`) — the harness detects a skill regression the strong model masks. Codex portability spot-check PASS (`CODEX`). Reproducible: re-run served from cache, $0 new, identical outcomes. Evidence dirs are disposable (`.runtime/eval/`), not canonical.
