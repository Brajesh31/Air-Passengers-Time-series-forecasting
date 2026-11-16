# 📜 Changelog

This log records changes to the project. It avoids publishing model scores unless they have been reproduced against a documented data split and environment.

## [Unreleased]

### Added
- A complete documentation index and expanded dataset, architecture, evaluation, installation, development, testing, and reproducibility guides.
- Runtime and development dependency manifests.
- A command-line forecasting workflow using seasonal Exponential Smoothing and SARIMA.
- Repository and forecast metric tests.
- Notebook syntax validation and GitHub Actions checks.

### Changed
- Rebuilt the notebook around continuous monthly dates, stationarity diagnostics, chronological holdout validation, baselines, seasonal models, and residual analysis.
- Removed the obsolete claim that the current workflow includes LSTM.

### Maintenance
- Removed hourly README timestamp automation that generated unnecessary commits.
