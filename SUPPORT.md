# 🆘 Support and Issue Reporting

## 1. Before asking for help

Read the root README and the relevant guide under `docs/`. Confirm that the project is running from the repository root and that the intended Python virtual environment is active.

Run the standard checks where possible:

```bash
python scripts/validate_notebook.py
python -m pytest
```

If the forecasting workflow is affected, also run:

```bash
python scripts/forecast.py --horizon 6 --test-months 24
```

These checks help distinguish environment problems from repository regressions. A passing test suite does not prove forecasting quality.

## 2. Choose the right issue type

Use the GitHub issue forms for:
- Bug reports.
- Feature requests.
- Documentation requests.

Before opening a new issue, search existing issues to avoid duplicates. For substantial changes, describe the problem and intended outcome before investing in a large implementation.

## 3. Information required for a useful bug report

Include as many of the following details as apply:

| Information | What to provide |
|---|---|
| Operating system | Windows, macOS, Linux and version |
| Python | Exact version |
| Git revision | Branch and commit SHA |
| Environment | Whether a virtual environment is active |
| Installation | Commands used to install dependencies |
| Entry point | Notebook name and cell number, or CLI command |
| Dataset | Schema, row count, and date range; no private data |
| Model | Model family, order, seasonal period, and horizon |
| Expected result | What you expected to happen |
| Actual result | What happened instead |
| Traceback | Complete sanitized error output |
| Reproduction | Minimal sequence of steps |

Do not include API keys, passwords, tokens, personal information, private datasets, or other sensitive material.

## 4. Reporting notebook problems

For notebook failures, state:
- Whether the kernel was restarted.
- Whether all cells were run in order.
- The failing cell number.
- The complete sanitized traceback.
- The working directory.
- The output of `import sys; print(sys.executable)`.
- Whether the dataset is the repository copy.

Static notebook validation does not execute notebook cells. A clean-kernel run is needed to diagnose runtime problems.

## 5. Reporting forecasting problems

For model or metric issues, include:
- Training start and end dates.
- Test start and end dates.
- Forecast horizon.
- Model orders and settings.
- Target units.
- Metrics and the exact prediction dates.
- Relevant convergence or numerical warnings.
- Baseline results, if available.

Do not report only a rounded metric without its test period and model configuration.

## 6. Documentation requests

A useful documentation issue identifies the file and section, explains what is missing or incorrect, and suggests what a reader needs to understand or do. The repository provides a dedicated documentation request form.

## 7. Security reports

Do not use public issues for vulnerabilities, exposed secrets, or sensitive exploit details. Follow [SECURITY.md](SECURITY.md) and use private GitHub vulnerability reporting where available.

## 8. Support boundaries

This is a community-maintained educational repository. Support is provided on a best-effort basis. No guaranteed response time, uptime, service-level agreement, or professional forecasting consultation is offered.

## 9. Helpful documentation

- [Installation](docs/installation.md)
- [Troubleshooting](docs/troubleshooting.md)
- [FAQ](docs/faq.md)
- [Testing](docs/testing.md)
- [Evaluation](docs/evaluation.md)
- [Contributing](CONTRIBUTING.md)
