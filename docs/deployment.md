# 🚀 Deployment and Operational-Use Boundaries

## 1. Current deployment status

This repository is a local educational analysis. It is designed to run in a Python environment through Jupyter or a command-line script.

It does not include:
- A web frontend or user-facing hosted application.
- An HTTP server or REST API.
- A database server.
- Scheduled or streaming data ingestion.
- Authentication or user accounts.
- A model registry or model-serving endpoint.
- Automated retraining.
- Production monitoring or alerting.
- Infrastructure-as-code or cloud deployment configuration.

The existence of this deployment guide does not mean that the project is deployed.

## 2. Local execution

Install dependencies as described in [installation.md](installation.md), then run:

```bash
python scripts/forecast.py --horizon 12 --test-months 24
```

The script writes local report, prediction, and plot files under `artifacts/`. These are run outputs, not production model artifacts.

## 3. Why the current workflow should not be operationalized

The dataset contains 144 monthly observations ending in 1960. It is not current and does not include the operational factors that influence present-day airline passenger demand.

A production forecast based on this data would be misleading regardless of whether the code runs successfully. Historical pattern fitting is not a substitute for current, relevant data and validation.

## 4. Requirements for a credible operational system

A real operational project would need a separate requirements and architecture process. At minimum, consider:

### Data governance
- Current and legally usable data sources.
- Defined owners and access permissions.
- Documented units, update cadence, quality rules, and retention.
- Versioned datasets and reproducible transformations.
- Privacy and commercial confidentiality review.

### Forecasting design
- Explicit forecast users and decisions.
- Defined targets, aggregation levels, and horizons.
- Baseline methods and acceptance criteria.
- Rolling-origin and seasonal backtesting.
- Prediction intervals and uncertainty communication.
- Monitoring for bias, drift, and degraded accuracy.

### Software architecture
- A documented service contract if an API is needed.
- Input validation and error semantics.
- Versioned model and data artifacts.
- Authentication and authorization.
- Logging, auditability, and observability.
- Failure handling, rollback, and recovery procedures.

### Operations
- Deployment environment and ownership.
- Scheduled retraining criteria.
- Model approval process.
- Alert thresholds and escalation.
- Backup and retention strategy.
- Cost and availability expectations.
- Security review and incident response.

## 5. Suggested staged approach

1. Define the business decision and forecast target.
2. Acquire and validate current data with clear permissions.
3. Establish naive and seasonal-naive baselines.
4. Design rolling-origin evaluation.
5. Compare candidate models on the same origins and horizons.
6. Quantify forecast uncertainty.
7. Obtain domain review and agree on acceptance criteria.
8. Only then design an API, database, or deployment environment if needed.
9. Monitor forecasts after launch and maintain rollback capability.

Do not begin with a cloud service or dashboard before the forecast itself has demonstrated value.

## 6. Local reproducibility

For local experiments, record the Git commit, data checksum, Python and package versions, model settings, train/test dates, metrics, and warnings. See [reproducibility.md](reproducibility.md).

## 7. Scope statement

No production deployment is currently supported or recommended by this repository. Any future deployment should be treated as a distinct project with its own requirements, data governance, security model, tests, and operational documentation.
