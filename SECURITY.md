# 🔐 Security Policy

## Scope

This repository contains Python scripts, Jupyter notebooks, documentation, and a historical CSV dataset. Notebooks and scripts execute code locally and should be reviewed before use.

## Reporting a vulnerability

Use GitHub's private vulnerability reporting feature when available:
https://github.com/Brajesh31/Air-Passengers-Time-series-forecasting/security/advisories/new

If private reporting is unavailable, contact the repository owner privately through GitHub. Do not publish secrets or sensitive details in a public issue.

Include the affected file, commit, environment, reproduction steps, impact, and sanitized evidence.

## Safe usage

- Use a virtual environment.
- Review notebook cells and downloaded packages before execution.
- Do not place credentials in notebook cells or committed environment files.
- Do not commit personal or restricted datasets.
- Review generated notebook outputs before publishing.
- Treat external CSV files as untrusted input and validate their schema and values.

## Dependency security

Install from the documented requirements files, keep dependencies reasonably current, and review security advisories before upgrades. The repository uses supported version ranges rather than a fully locked environment.
