# 📦 Installation and Environment Setup

## 1. Purpose

This guide explains how to create an isolated Python environment, install the dependencies declared by the repository, open the notebook, and run the command-line forecasting workflow. Commands assume that the terminal is opened at the repository root unless a section says otherwise.

## 2. Prerequisites

- Python 3.10 or newer is recommended. CI currently uses Python 3.11.
- pip, normally included with Python.
- Python virtual environment support.
- Git for cloning the repository.
- A supported terminal.
- Internet access during initial package installation.
- A browser for Jupyter Notebook or JupyterLab.

Check the installed versions:

```bash
python --version
python -m pip --version
git --version
```

On Windows, the Python launcher can be used:

```powershell
py --version
```

## 3. Clone the repository

```bash
git clone https://github.com/Brajesh31/Air-Passengers-Time-series-forecasting.git
cd Air-Passengers-Time-series-forecasting
```

Check that the expected files are present:

```text
AirPassengers.csv
TimeSeriesForecasting.ipynb
requirements.txt
requirements-dev.txt
scripts/
tests/
docs/
```

Do not run the notebook from an arbitrary directory. The notebook reads the dataset using a repository-relative path.

## 4. Create a virtual environment

A virtual environment prevents this project's dependencies from interfering with other Python projects.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation because of the current execution policy, use the Python executable inside the environment directly or follow the operating system's documented virtual-environment guidance. Do not weaken system security settings broadly just to activate one environment.

### Windows Command Prompt

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

### macOS and Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, verify that Python resolves to the environment:

```bash
python -c "import sys; print(sys.executable)"
```

## 5. Upgrade pip and install runtime dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The runtime manifest currently includes the numerical, data, plotting, modelling, notebook, and notebook-format packages used by the project.

## 6. Install development dependencies

Contributors and maintainers should also install the development requirements:

```bash
python -m pip install -r requirements-dev.txt
```

The development manifest includes the runtime requirements plus pytest and notebook conversion/validation tooling. It does not replace the need to run the actual checks documented in [testing.md](testing.md).

## 7. Verify the installation

Check that the core packages import:

```bash
python -c "import numpy, pandas, matplotlib, seaborn, sklearn, statsmodels, nbformat; print('Core imports successful')"
```

Check the notebook file and dataset:

```bash
python -c "from pathlib import Path; assert Path('AirPassengers.csv').is_file(); assert Path('TimeSeriesForecasting.ipynb').is_file(); print('Project inputs found')"
```

Run the automated checks after installing development requirements:

```bash
python scripts/validate_notebook.py
python -m pytest
```

## 8. Launch the notebook

From the repository root:

```bash
jupyter notebook
```

Open `TimeSeriesForecasting.ipynb`. Restart the kernel and use **Run All**. If using JupyterLab, the equivalent command is:

```bash
jupyter lab
```

Run cells in order because later sections depend on variables and model objects defined earlier.

## 9. Run the CLI workflow

```bash
python scripts/forecast.py --horizon 12 --test-months 24
```

Optional custom dataset path:

```bash
python scripts/forecast.py --data path/to/AirPassengers.csv --horizon 6 --test-months 24
```

The script writes generated files to `artifacts/`. The directory is created during a successful run and ignored by Git.

## 10. Dependency versioning

The current requirements files specify compatible version ranges, not exact reproducible pins. This is convenient for installation but means two users may resolve different patch or minor releases over time. Record Python and package versions with any published result. A lock file should only be introduced after testing a chosen environment across the supported platforms.

## 11. Updating packages safely

Do not upgrade every package blindly and assume the result is correct. For a dependency update:

1. Review the package release notes and security advisories.
2. Update the relevant requirement range.
3. Recreate the environment or install into a clean environment.
4. Run import checks, notebook validation, unit tests, and CLI smoke tests.
5. Execute the notebook from a clean kernel if analytical dependencies changed.
6. Compare model outputs if numerical package versions changed.
7. Document meaningful compatibility changes.

Dependabot is configured to propose monthly dependency updates. A proposed update still requires review and CI evidence.

## 12. Deactivate and remove the environment

When finished:

```bash
deactivate
```

To remove the environment, delete the local `.venv/` directory. It is not project source and is excluded from Git.

## 13. Troubleshooting

If installation fails, confirm the Python version, activate the intended environment, upgrade pip, and inspect the complete package error. Do not mix packages installed globally with packages in the virtual environment. See [troubleshooting.md](troubleshooting.md) for more targeted diagnosis.
