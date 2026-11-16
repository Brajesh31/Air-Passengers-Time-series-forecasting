# 🔧 Repository Maintenance Guide

## 1. Purpose

This guide defines routine maintenance expectations for the repository. Maintenance should keep the project understandable, installable, testable, and honest about its capabilities. It should not introduce unrelated features or alter analytical behaviour without a clear reason.

## 2. Routine review areas

Review these areas when maintaining the repository:

- Dataset integrity and documented provenance.
- Notebook execution from a clean kernel.
- CLI argument handling and error messages.
- Runtime and development dependency ranges.
- Automated tests and CI configuration.
- Documentation links and command examples.
- GitHub issue forms and pull request template.
- Security and governance guidance.
- Generated outputs and ignored files.
- Roadmap and changelog accuracy.

## 3. Dependency maintenance

Dependabot is configured for monthly pip and GitHub Actions updates. Each proposed update should be reviewed for compatibility and security impact.

For each dependency update:

1. Review release notes and known vulnerabilities.
2. Check Python-version compatibility.
3. Apply the update in a clean environment.
4. Run notebook static validation.
5. Run pytest.
6. Run the CLI smoke test.
7. Execute the notebook if numerical or plotting packages changed.
8. Record any material numerical differences.
9. Update the dependency range only when the tested version is supported.

Do not merge dependency updates solely because installation succeeded.

## 4. CI maintenance

The current workflow checks out the repository, sets up Python 3.11, installs development dependencies, validates notebook structure and syntax, runs pytest, and executes a CLI smoke test.

When changing CI:

- Keep permissions minimal.
- Pin actions to reviewed major versions or immutable SHAs according to repository policy.
- Ensure commands exist and are valid from the repository root.
- Do not create a success-only workflow that skips meaningful checks.
- Review logs for warnings and skipped steps.
- Confirm that a green run corresponds to the latest relevant commit.

CI does not execute the full notebook or certify model accuracy.

## 5. Documentation maintenance

Whenever project behaviour changes:

- Update the root README if the change affects user-facing behaviour.
- Update the relevant technical guide.
- Update the documentation index if a page is added or removed.
- Update examples and command arguments.
- Update the changelog.
- Check relative links and code paths.
- Label future work as planned, not implemented.
- Remove claims about capabilities that no longer exist.

Do not retain empty or generic API, database, or deployment instructions when the project does not implement those systems. The current pages explicitly document that absence.

## 6. Dataset maintenance

Never replace the CSV without checking source, licence, units, date coverage, schema, monthly continuity, duplicates, missing values, and checksum. Review whether the existing tests still describe the intended data. A dataset update can invalidate previously reported metrics and model conclusions.

## 7. Notebook maintenance

Run the notebook from a clean kernel after changes. Review cell order, outputs, charts, warnings, paths, and metadata. Remove stale outputs where they may mislead readers. Static syntax validation alone is not enough.

## 8. Release and versioning

The project does not currently define a formal release process or published package. If a tagged release is introduced, define versioning rules, release notes, supported Python versions, dependency expectations, and a reproducibility record first.

Do not update the citation version merely because a documentation file changed unless the project adopts and follows a versioning policy.

## 9. Security and repository hygiene

Do not commit environment secrets, personal data, local virtual environments, generated artifacts, caches, or editor state. Review new dependencies and notebook code before execution. Use private reporting for vulnerabilities.

## 10. Maintenance checklist

- [ ] Default branch is clean and expected.
- [ ] No accidental generated files are tracked.
- [ ] Dataset schema and monthly continuity are valid.
- [ ] Notebook static validation passes.
- [ ] Notebook runs from a clean kernel when relevant.
- [ ] Unit tests pass.
- [ ] CLI smoke test passes.
- [ ] GitHub Actions result is successful for the latest relevant commit.
- [ ] Dependency proposals are reviewed.
- [ ] README and documentation index are current.
- [ ] Relative links resolve.
- [ ] Changelog and roadmap reflect reality.
- [ ] No unsupported feature claims remain.

## 11. Maintenance ownership

The repository identifies Brajesh Kumar as maintainer through its governance and ownership files. Contributors should use the issue and pull request processes described in [CONTRIBUTING.md](../CONTRIBUTING.md).
