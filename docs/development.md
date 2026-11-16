# 🛠️ Development Guide

## Project layout

- `TimeSeriesForecasting.ipynb`: educational walkthrough and visual analysis.
- `scripts/forecast.py`: reusable command-line forecasting workflow.
- `AirPassengers.csv`: historical monthly dataset.
- `tests/`: loader, metric, and repository tests.
- `docs/`: project and methodology guidance.

## Development principles

1. Preserve chronological ordering.
2. Never shuffle a time series for model evaluation.
3. Fit transformations only on the training window.
4. Compare with naive and seasonal-naive baselines.
5. Use explicit month-start timestamps and a documented monthly frequency.
6. Report the test window and forecast horizon with every metric.
7. Keep model parameters and package versions reproducible.
8. Do not suppress all warnings during model development. Review convergence and stationarity warnings.
9. Remove stale outputs after changing analytical logic.
10. Keep the README and docs aligned with actual implemented methods.

## Local checks

```bash
python scripts/validate_notebook.py
python -m pytest
python scripts/forecast.py --horizon 12 --test-months 24
```

## Pull request expectations

Include the motivation, affected notebook or script, data assumptions, train/test boundaries, model parameters, validation evidence, metric changes, and limitations. Do not claim improved performance unless the same validation protocol supports the comparison.

## Scope

This is a notebook and command-line educational project. A network API or database is not part of the current architecture. Do not add infrastructure without a concrete use case.
