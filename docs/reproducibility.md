# 🔁 Reproducibility and Experiment Records

## 1. What reproducibility means here

A reproducible analysis is one where another person can identify the input data, code version, environment, modelling choices, evaluation window, and commands needed to recreate the reported result.

Re-running the same notebook is not enough if the dataset, package versions, kernel state, model parameters, or train/test boundary are unknown.

## 2. Current environment declarations

The repository declares dependency ranges in `requirements.txt` and development tools in `requirements-dev.txt`. These files provide installation guidance, but they are not a complete lock file. Package resolution can change over time within the declared ranges.

Record the exact versions used for any report:

```bash
python --version
python -m pip freeze
```

For a clean reproduction, create a new virtual environment rather than relying on a long-lived environment with unknown packages.

## 3. Dataset identity

Record:

- Dataset filename.
- Exact source and source version, once verified.
- Retrieval or release date, if known.
- Number of observations.
- First and last observation dates.
- Column names and target units.
- Any date normalization or transformations.
- Cryptographic checksum.

A checksum can be generated locally:

```bash
python -c "import hashlib; from pathlib import Path; p=Path('AirPassengers.csv'); print(hashlib.sha256(p.read_bytes()).hexdigest())"
```

Do not invent provenance if the original source has not been verified.

## 4. Environment setup

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Record the operating system, Python version, and package versions. For long-lived research, consider producing a tested lock file or environment export and retaining it with the experiment record.

## 5. Reproducing the notebook

1. Check out the desired Git commit.
2. Confirm the dataset file matches the intended version.
3. Activate a clean environment.
4. Install dependencies.
5. Start Jupyter from the repository root.
6. Open the notebook.
7. Restart the kernel.
8. Run all cells in order.
9. Review warnings, output, plots, and metrics.
10. Save the notebook only if the resulting output is intentionally part of the change.

Notebook execution can produce environment-specific rendering differences. Record any warnings and do not silently discard failed cells.

## 6. Reproducing the CLI workflow

Default-style run:

```bash
python scripts/forecast.py --horizon 12 --test-months 24
```

A smaller smoke run:

```bash
python scripts/forecast.py --horizon 6 --test-months 24
```

The script writes output files to `artifacts/`. Preserve copies of the output report and prediction files with the experiment record if they are needed for review. The generated directory is ignored by Git and is not automatically uploaded.

## 7. Required experiment metadata

For each reported experiment, record:

| Field | Example or description |
|---|---|
| Run identifier | A unique human-readable label |
| Git commit | Full commit SHA |
| Dataset | File, version, checksum |
| Python | Exact version |
| Packages | Exact resolved package versions |
| Platform | OS and architecture |
| Training range | First and last training month |
| Test range | First and last test month |
| Horizon | Forecast months |
| Model | Model family and all parameters |
| Diagnostics | Warnings and convergence information |
| Metrics | MAE, RMSE, MAPE with units/context |
| Output | Location of report and prediction artifacts |
| Notes | Deviations, failures, interpretation |

## 8. Randomness and numerical variation

The current models are classical statistical methods and do not use an explicit neural-network training seed. Nevertheless, numerical libraries, solver implementations, package versions, and hardware can affect results. Do not promise bit-for-bit identity across all environments without testing it.

If a future stochastic model is added, document all random seeds, deterministic settings, hardware dependencies, and remaining sources of nondeterminism.

## 9. Avoiding data leakage

- Do not fit scalers, imputers, decompositions, or other learned transformations on the full dataset before splitting.
- Do not choose model orders using the final holdout.
- Do not use future observations to repair historical input values without documenting the procedure.
- Do not report in-sample fit metrics as out-of-sample forecast accuracy.
- Keep all dates in chronological order.

## 10. Reproduction checklist

- [ ] Commit SHA recorded.
- [ ] Dataset source/version recorded.
- [ ] Dataset checksum recorded.
- [ ] Python and package versions recorded.
- [ ] Notebook run from a clean kernel, if applicable.
- [ ] Training and test dates recorded.
- [ ] Forecast horizon and model parameters recorded.
- [ ] Warnings and failed runs recorded.
- [ ] Metrics and units reported.
- [ ] Limitations and deviations documented.

## 11. Reproducibility limitations

The project does not currently ship a fully locked dependency environment, verified dataset provenance record, experiment-tracking service, or immutable model artifact registry. Reproduction therefore requires recording these details at run time.
