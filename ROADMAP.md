# 🗺️ Project Roadmap

## Purpose

This roadmap records possible improvements to the historical AirPassengers forecasting learning project. Items are proposals until implemented, tested, and documented. A roadmap entry must not be described in the README as an existing capability.

## Completed foundations

- [x] Include the historical monthly AirPassengers CSV.
- [x] Provide a guided Jupyter analysis notebook.
- [x] Provide a local Python command-line forecasting reference.
- [x] Validate required input columns and monthly continuity in the CLI loader.
- [x] Demonstrate naive and seasonal-naive baselines in the notebook.
- [x] Include seasonal Exponential Smoothing and SARIMA examples.
- [x] Calculate MAE, RMSE, and supplementary MAPE for a chronological holdout.
- [x] Add notebook format and static syntax validation.
- [x] Add unit and repository tests.
- [x] Add a CI workflow with a CLI smoke test.
- [x] Add installation, architecture, data, evaluation, development, testing, and reproducibility guides.
- [x] Add GitHub issue templates, contribution guidance, security policy, and dependency update configuration.
- [x] Expand the project documentation with methodology, model reference, notebook walkthrough, experiment protocol, results interpretation, data dictionary, glossary, and maintenance guidance.

## Priority 1: stronger analytical validation

- [ ] Implement rolling-origin or expanding-window backtesting with clearly defined forecast origins.
- [ ] Report naive and seasonal-naive baselines in the CLI output using the same holdout dates.
- [ ] Add tests for malformed dates, missing months, duplicate months, non-numeric values, invalid horizons, and invalid split sizes.
- [ ] Add residual autocorrelation diagnostics and document their interpretation.
- [ ] Compare model performance by forecast horizon rather than only one aggregate score.
- [ ] Add prediction intervals only with a documented method and interval coverage evaluation.

## Priority 2: reproducibility and data governance

- [ ] Verify the exact upstream dataset source and redistribution licence.
- [ ] Add a source citation, retrieval/version details, and a checksum once independently verified.
- [ ] Evaluate a fully locked dependency environment on supported platforms.
- [ ] Define a repeatable experiment report format and retain representative, non-misleading run metadata.
- [ ] Add CI coverage for additional supported Python versions after compatibility is tested.
- [ ] Consider a clean-kernel notebook execution job if runtime and stability costs are acceptable.

## Priority 3: learning and documentation quality

- [ ] Add a worked rolling-origin example after the implementation exists.
- [ ] Add a documented comparison of additive and multiplicative seasonal assumptions.
- [ ] Add an explanation of forecast interval coverage and calibration if intervals are implemented.
- [ ] Add accessible alternative text or descriptions for important notebook plots.
- [ ] Add a short learning path for readers new to time-series concepts.

## Explicitly out of scope unless a concrete need is approved

- Production airline-demand forecasting.
- Current airline market predictions from the 1949-1960 series.
- Passenger-level or confidential commercial data.
- REST API or web application.
- Database server or cloud data warehouse.
- Automated production ingestion and retraining.
- Model serving, registry, or operational alerting.
- Neural networks added only for complexity or presentation value.

These components would require separate requirements, data governance, validation evidence, security review, and operational ownership.

## Roadmap policy

Prioritize correctness, honest evaluation, and reproducibility over the number of files, frameworks, or models. Close an item only after its implementation, tests, documentation, and limitations have been reviewed.
