# 🚀 Deployment and Operational Use

## Current status

The repository is a local notebook and command-line educational analysis. It does not include a web service, API, database, scheduled data ingestion, model registry, or production deployment.

## Local execution

```bash
python -m pip install -r requirements.txt
python scripts/forecast.py --horizon 12 --test-months 24
```

Outputs are written to `artifacts/`.

## Requirements before production use

A credible operational forecasting system would require:
- Current, governed passenger-demand data.
- Airline, route, capacity, schedule, fare, and disruption features where relevant.
- Rolling-origin and seasonal backtesting.
- Prediction intervals and uncertainty communication.
- Monitoring for drift and forecast error.
- Versioned models, datasets, and code.
- Retraining and rollback policies.
- Access controls and audit logs.
- Domain-owner review and clear acceptance criteria.

Do not deploy the historical teaching forecasts as an operational planning service.
