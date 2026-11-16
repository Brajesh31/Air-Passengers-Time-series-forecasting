# 📚 Project Documentation

This documentation set explains how to install, understand, run, evaluate, test, reproduce, and maintain the Air Passengers Time-Series Forecasting repository. It is written for learners, reviewers, contributors, and anyone attempting to reproduce an analysis from the checked-in historical dataset.

## Start here

| If you want to... | Read |
|---|---|
| Understand what the repository does | [Architecture](architecture.md), [Notebook walkthrough](notebook-guide.md) |
| Understand the CSV and its limitations | [Data documentation](data.md), [Data dictionary](data-dictionary.md) |
| Install and run the project | [Installation](installation.md), [Development guide](development.md) |
| Understand the statistical methods | [Forecasting methodology](methodology.md), [Model reference](models.md) |
| Evaluate and compare forecasts | [Evaluation protocol](evaluation.md), [Experiment protocol](experiment-protocol.md), [Interpreting results](results-interpretation.md) |
| Reproduce a result | [Reproducibility](reproducibility.md) |
| Run and understand tests | [Testing](testing.md) |
| Resolve a local issue | [Troubleshooting](troubleshooting.md), [FAQ](faq.md) |
| Understand deployment boundaries | [Deployment](deployment.md), [API status](api.md), [Persistence](database.md) |
| Understand terms used in the project | [Glossary](glossary.md) |
| Maintain the repository | [Maintenance guide](maintenance.md) |

## Technical documentation

- [Architecture](architecture.md)
- [Notebook walkthrough](notebook-guide.md)
- [Dataset and provenance](data.md)
- [Data dictionary](data-dictionary.md)
- [Forecasting methodology](methodology.md)
- [Model reference](models.md)
- [Evaluation protocol](evaluation.md)
- [Experiment protocol](experiment-protocol.md)
- [Interpreting results](results-interpretation.md)
- [Reproducibility](reproducibility.md)
- [Testing](testing.md)
- [Glossary](glossary.md)

## Working with the repository

- [Installation](installation.md)
- [Development](development.md)
- [Maintenance](maintenance.md)
- [Troubleshooting](troubleshooting.md)
- [FAQ](faq.md)

## Project status and governance

- [Deployment boundaries](deployment.md)
- [API status](api.md)
- [Database and persistence status](database.md)
- [Roadmap](../ROADMAP.md)
- [Changelog](../CHANGELOG.md)
- [Contributing](../CONTRIBUTING.md)
- [Security policy](../SECURITY.md)
- [Support](../SUPPORT.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [License](../LICENSE)

## Documentation conventions

- A guide describes current behaviour only when that behaviour exists in the repository.
- Proposed improvements are labelled as future work, not as implemented features.
- Commands are written for execution from the repository root unless stated otherwise.
- Paths use repository-relative notation.
- Forecast metrics must always be accompanied by the evaluation window and target units.
- Historical observations and illustrative model outputs must not be presented as current airline intelligence.

## Project boundary

This repository is a local educational analysis built around one small historical monthly series. It is not a deployed application. It currently has no network API, database server, automated data ingestion, scheduled retraining, model registry, or production monitoring. The API and database guides explicitly document those absences so readers are not misled by empty or speculative technical documentation.

For the high-level project description, installation commands, and primary entry points, begin with the [root README](../README.md).
