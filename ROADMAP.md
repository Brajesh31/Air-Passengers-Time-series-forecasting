# 🗺️ Roadmap

## Completed foundations
- [x] Document the included historical dataset and monthly schema.
- [x] Add runtime and development dependency manifests.
- [x] Add command-line seasonal forecasting workflow.
- [x] Add tests for dataset validation and forecast metrics.
- [x] Add notebook syntax and repository CI checks.
- [x] Add chronological holdout model comparisons and baseline forecasts.

## Future improvements
- [ ] Add rolling-origin backtesting across multiple forecast origins.
- [ ] Add seasonal-naive benchmark reporting in the CLI output.
- [ ] Add prediction intervals and coverage evaluation.
- [ ] Add parameter sensitivity analysis for SARIMA and Exponential Smoothing.
- [ ] Add a fully locked environment after validation on supported platforms.
- [ ] Add dataset provenance, source licence, and checksum evidence.
- [ ] Add model residual autocorrelation diagnostics.
- [ ] Consider neural-network experiments only with a justified validation design and small-sample limitations clearly stated.

## Scope boundary

The repository remains a historical forecasting learning project. Production API, data ingestion, and model serving are not planned without a concrete operational use case.
