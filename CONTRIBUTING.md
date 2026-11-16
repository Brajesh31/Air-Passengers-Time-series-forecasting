# 🤝 Contributing

Thank you for considering a contribution. This project is an educational time-series analysis of the historical AirPassengers dataset. Contributions should improve correctness, clarity, reproducibility, maintainability, or learning value without overstating what the data can support.

## 📑 Contents

- [Before You Start](#-before-you-start)
- [Ways to Contribute](#-ways-to-contribute)
- [Development Setup](#-development-setup)
- [Notebook and Analysis Standards](#-notebook-and-analysis-standards)
- [Forecasting Validation Standards](#-forecasting-validation-standards)
- [Testing Checklist](#-testing-checklist)
- [Documentation Standards](#-documentation-standards)
- [Pull Request Process](#-pull-request-process)
- [Maintainer](#-maintainer)

## 🔍 Before You Start

- Search existing issues and pull requests to avoid duplicated work.
- Open an issue before making a large or behaviour-changing proposal.
- Read the README and the relevant guide under `docs/`.
- Keep changes focused and explain the reason for them.
- Do not include credentials, private data, or unrelated generated files.

## 💡 Ways to Contribute

- Correct unclear or inaccurate explanations.
- Improve data validation and error reporting.
- Add tests for existing behaviour.
- Improve notebook readability and reproducibility.
- Improve model evaluation without introducing temporal leakage.
- Improve accessibility of plots and documentation.
- Report reproducible bugs or documentation gaps.

## 🧰 Development Setup

Use a virtual environment and install the development requirements:

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Run the project checks:

```bash
python scripts/validate_notebook.py
python -m pytest
python scripts/forecast.py --horizon 6 --test-months 24
```

## 📓 Notebook and Analysis Standards

- Run the notebook from a clean kernel.
- Execute cells in their intended order.
- Keep narrative explanations consistent with the implementation.
- Avoid hiding warnings during model development.
- Remove stale outputs when they may misrepresent the current code.
- Label axes, units, dates, and forecast horizons clearly.
- Explain diagnostic tests and their assumptions.
- Do not claim a method is implemented unless it appears in the actual notebook or scripts.

## 📉 Forecasting Validation Standards

Time-series validation must respect temporal order.

1. Do not shuffle observations for train/test evaluation.
2. Keep all training observations earlier than all test observations.
3. Fit preprocessing and model parameters using training observations only.
4. Compare against simple naive and seasonal-naive benchmarks.
5. Use the same validation windows when comparing candidate models.
6. Report the training end date, test period, forecast horizon, and seasonal period.
7. Report MAE and RMSE in the target units. Treat MAPE as supplementary.
8. Use rolling-origin or expanding-window evaluation when making broader model comparisons.
9. Inspect residual patterns and convergence warnings.
10. Do not repeatedly tune against the final holdout and then present it as an unbiased test.

A lower error on one historical split is not proof of general forecasting superiority.

## ✅ Testing Checklist

Before submitting a change, run the relevant checks:

- [ ] `python scripts/validate_notebook.py`
- [ ] `python -m pytest`
- [ ] `python scripts/forecast.py --horizon 6 --test-months 24` when the forecasting path is affected
- [ ] Notebook executed from a clean kernel when notebook logic changes
- [ ] No accidental data, output, or environment files are included
- [ ] Documentation links and code examples were reviewed

Static notebook validation parses structure and syntax. It does not execute the analysis cells.

## 📝 Documentation Standards

- Use descriptive headings and valid relative links.
- Include commands that match the actual repository.
- Distinguish implemented functionality from future ideas.
- State data and model limitations.
- Keep README structure and file lists synchronized with the repository.
- Update `CHANGELOG.md` when a user-visible change is made.
- Avoid placeholder pages and unsupported API, database, or deployment claims.

## 🔀 Pull Request Process

1. Describe the problem and the scope of the change.
2. Explain any changes to dataset assumptions or evaluation design.
3. Include the commands and results used for validation.
4. Update relevant documentation.
5. Complete the repository pull request template.
6. Keep the diff focused and review generated notebook output carefully.

A contribution may be asked for revision when it introduces temporal leakage, undocumented assumptions, unsupported claims, or unnecessary complexity.

## 👤 Maintainer

**Brajesh Kumar**  
GitHub: [@Brajesh31](https://github.com/Brajesh31)
