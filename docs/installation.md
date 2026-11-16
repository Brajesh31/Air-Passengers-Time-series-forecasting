# 📦 Installation

## Requirements

- Python 3.10 or newer is recommended.
- pip and virtual environment support.
- Git for cloning the repository.
- Jupyter for notebook execution.

## Create an environment

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For development checks:

```bash
python -m pip install -r requirements-dev.txt
```

## Launch the notebook

Run Jupyter from the repository root:

```bash
jupyter notebook
```

Open `TimeSeriesForecasting.ipynb`. The notebook reads `AirPassengers.csv` using a relative path.

## Run the forecasting script

```bash
python scripts/forecast.py --horizon 12 --test-months 24
```

The script writes generated artifacts under `artifacts/`. They are local outputs and are ignored by Git.

## Version note

Requirements use compatible version ranges rather than exact pins. For formal reproducibility, record actual installed versions or produce a fully locked environment after testing on the target platform.
