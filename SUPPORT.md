# 🆘 Support

For a bug report or question, include:
- Operating system and Python version.
- Installation command and package versions.
- Notebook name and cell number, or CLI command.
- Full sanitized traceback.
- Expected behaviour and actual behaviour.
- Dataset schema and date range, without private data.
- Train/test boundaries and model parameters where relevant.

Run these checks before reporting an issue:

```bash
python scripts/validate_notebook.py
python -m pytest
```

For security issues, follow [SECURITY.md](SECURITY.md) and do not post secrets publicly.
