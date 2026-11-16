# 🔐 Security Policy

## 1. Scope

This repository contains Python scripts, Jupyter notebook code, documentation, GitHub workflow configuration, dependency manifests, and a historical CSV dataset. It is primarily intended for local educational use.

The project does not currently operate a hosted application, public API, database, authentication service, or production infrastructure. Security reports should identify the actual repository component affected rather than assume those services exist.

## 2. Supported maintenance scope

Security fixes are considered for the current default branch. The maintainer may also review a report affecting a prior commit if the issue remains relevant and reproducible. No formal long-term support schedule or release support matrix is currently published.

## 3. Reporting a vulnerability

Please use GitHub's private vulnerability reporting feature when it is available:

https://github.com/Brajesh31/Air-Passengers-Time-series-forecasting/security/advisories/new

If private reporting is unavailable, contact the repository maintainer privately through GitHub. Do not create a public issue containing exploit instructions, credentials, personal data, or details that would expose another system.

A useful report includes:

- Affected file, dependency, workflow, or commit.
- Python, operating system, and package versions where relevant.
- Reproduction steps that do not expose secrets.
- Expected and observed behaviour.
- Security impact and realistic attack scenario.
- Sanitized logs, screenshots, or proof-of-concept evidence.
- Any known mitigation.

Please allow time for the maintainer to investigate before publicly disclosing a vulnerability.

## 4. Notebook execution risks

Jupyter notebooks can execute arbitrary local Python code. Review notebook cells before running notebooks obtained from an untrusted source. Be cautious with shell commands, file operations, package installation commands, network access, and code that reads environment variables.

Notebook output can also contain sensitive information. Inspect outputs and metadata before committing or sharing a notebook.

## 5. Input data risks

The current CSV is a local input. If users supply a different CSV, treat it as untrusted input. Validate its schema, types, dates, numeric values, size, and monthly continuity. Do not assume a file is safe merely because it has a `.csv` extension.

Do not commit customer records, passenger-level data, booking details, personal information, or commercially restricted datasets.

## 6. Secrets and configuration

The current project does not require API keys or credentials. The `.env.example` file explains this. Never add real credentials to:
- Notebook cells or outputs.
- Python scripts.
- GitHub Actions YAML.
- Committed environment files.
- Issue reports or pull request descriptions.

Use GitHub-managed secrets only if a future workflow genuinely requires them, and grant the narrowest permissions possible.

## 7. Dependency security

Runtime and development packages are declared in `requirements.txt` and `requirements-dev.txt`. Dependabot is configured for monthly pip and GitHub Actions update proposals.

Review package advisories and release notes before accepting upgrades. Run the test suite and CLI smoke test after updates. Dependency version ranges are not a substitute for reviewing vulnerabilities or maintaining a tested environment.

## 8. GitHub Actions permissions

The CI workflow currently uses read-only repository content permission. Do not add write permissions unless a specific automation requires them. New workflows should use least privilege, avoid printing secrets, and avoid executing untrusted pull-request code with privileged credentials.

## 9. Safe local practices

- Use a virtual environment.
- Keep Python and dependencies reasonably current.
- Review notebook code before execution.
- Validate external input files.
- Avoid running commands copied from untrusted issue comments.
- Keep private files outside the repository.
- Review generated outputs before committing.
- Do not disable security checks to force a passing build.

## 10. Incident handling

If a secret is committed, deleting it from the latest commit is not enough. Revoke or rotate the exposed credential first, then remove it from repository history where appropriate and review logs for misuse. Do not paste the exposed value into a public issue.

## 11. Policy changes

Security policy changes should be reflected in this file and in the repository's actual workflows and configuration. Do not claim that a scanner, monitoring service, or vulnerability response SLA exists unless it has been configured and verified.
