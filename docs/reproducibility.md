# 🔁 Reproducibility

## Environment

The project declares dependency ranges in `requirements.txt` and development tools in `requirements-dev.txt`. These provide installation guidance but are not a fully locked environment. Record exact Python and package versions when publishing a result.

## Install

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## Run the notebook

Start Jupyter from the repository root, open `TimeSeriesForecasting.ipynb`, restart the kernel, and run all cells in order.

## Run the command-line reference workflow

```bash
python scripts/forecast.py --horizon 12 --test-months 24
```

The script writes a JSON summary, CSV predictions, and a plot under the ignored `artifacts/` directory.

## Experiment record

For each reported run, record:
- Git commit SHA.
- Python version and operating system.
- Package versions.
- Dataset checksum and date range.
- Chronological train/test boundaries.
- Forecast horizon and seasonal period.
- Model orders and parameters.
- MAE, RMSE, and supplementary metrics.
- Any warnings, convergence issues, and failed runs.

## Determinism

Classical statistical models are generally less dependent on random seeds than neural networks, but solver behaviour, package versions, numerical libraries, and hardware can still affect outputs. If a neural-network workflow is reintroduced, set all relevant random seeds and record runtime hardware and library versions.

## Evaluation boundary

The final holdout period must remain outside model selection. For robust model comparison use rolling-origin or expanding-window backtests, not a single test split alone.
