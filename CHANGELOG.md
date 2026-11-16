# 📜 Changelog

This changelog records material repository changes. It is not a record of every line edit, and it must not imply that documentation work independently improves forecast accuracy.

## [Unreleased]

### Documentation
- Expanded the documentation index and added detailed guides for notebook execution, forecasting methodology, model specifications, data dictionary, experiment protocol, result interpretation, glossary, and repository maintenance.
- Expanded architecture, dataset, installation, development, evaluation, reproducibility, testing, troubleshooting, FAQ, deployment, API, and database documentation.
- Clarified the distinction between the notebook and CLI workflows.
- Clarified which forecasting methods are implemented and which are not.
- Added explicit limitations around historical data, model validation, production use, and missing infrastructure.
- Expanded contributor, security, support, and code-of-conduct guidance.
- Updated the roadmap to distinguish completed work from future proposals.

### GitHub repository maintenance
- Added a documentation-request issue form.
- Added monthly Dependabot update configuration for pip and GitHub Actions.
- Expanded the root README with project scope, setup, methods, data, CLI usage, generated outputs, testing, and limitations.
- Removed a redundant tracked editor-specific ignore file.

### Verification
- Reviewed the README's relative links against the repository tree.
- Inspected the CI workflow and its validation steps.
- Confirmed successful CI runs for the repository maintenance commits.
- Static notebook validation and CI smoke tests do not execute the entire notebook or prove forecasting generalization.

## Historical repository notes

Earlier repository work introduced or revised the local command-line forecasting reference, dependency manifests, tests, documentation, and CI checks. Consult Git history for the exact chronology of those changes. This current documentation expansion does not claim to have created or independently validated the forecasting algorithms.

## Changelog policy

- Group changes by documentation, features, fixes, and maintenance where useful.
- Record user-visible changes and important compatibility changes.
- Do not claim a model is more accurate without comparable evaluation evidence.
- Do not claim a service, database, API, or production deployment exists unless it is implemented and verified.
- Keep future work in the roadmap until it has been delivered.
