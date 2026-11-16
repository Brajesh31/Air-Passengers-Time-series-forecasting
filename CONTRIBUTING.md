# 🤝 Contributing

Thanks for helping improve this forecasting project. Contributions should strengthen analytical correctness, temporal validation, reproducibility, and clarity.

## Before contributing

- Read the notebook and relevant documentation.
- Preserve monthly chronology.
- Check data schema, frequency, units, and gaps.
- Explain model and parameter choices.
- Compare against naive and seasonal-naive baselines.
- Do not tune against the final holdout set.
- Do not commit credentials or unrelated datasets.

## Development setup

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_notebook.py
python -m pytest
```

## Notebook standards

- Run from a clean kernel and execute cells in order.
- Avoid hiding warnings during model development.
- Clear stale outputs when they could mislead readers.
- Record dataset, train/test dates, forecast horizon, model order, package versions, and metrics.
- Keep the notebook explanations consistent with implemented code.

## Pull request checklist

- [ ] The motivation and scope are clear.
- [ ] Time ordering is preserved.
- [ ] No future data leaks into preprocessing or training.
- [ ] A baseline is included for forecast comparisons.
- [ ] Validation uses a documented holdout or rolling-origin strategy.
- [ ] Metrics and units are explained.
- [ ] The notebook and scripts pass repository checks.
- [ ] Documentation and CHANGELOG are updated.
- [ ] No secrets or private data are included.

Do not claim an improvement unless the same validation protocol supports it.
