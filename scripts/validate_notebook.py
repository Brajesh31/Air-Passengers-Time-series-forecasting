#!/usr/bin/env python3
"""Validate notebook JSON and Python syntax without executing notebook cells."""
from __future__ import annotations

import ast
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted(ROOT.glob("*.ipynb"))


def remove_ipython_lines(source: str) -> str:
    cleaned = []
    for line in source.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("%", "!")):
            cleaned.append("# IPython command omitted from static syntax validation")
        else:
            cleaned.append(line)
    return "\n".join(cleaned)


def main() -> int:
    if not NOTEBOOKS:
        print("No root-level notebooks found.", file=sys.stderr)
        return 1

    errors: list[str] = []
    for path in NOTEBOOKS:
        try:
            notebook = nbformat.read(path, as_version=4)
            nbformat.validate(notebook)
        except Exception as exc:
            errors.append(f"{path.name}: invalid notebook: {exc}")
            continue

        for index, cell in enumerate(notebook.cells, start=1):
            if cell.cell_type != "code" or not cell.source.strip():
                continue
            try:
                ast.parse(remove_ipython_lines(cell.source), filename=f"{path.name}:cell-{index}")
            except SyntaxError as exc:
                errors.append(f"{path.name}: cell {index}, line {exc.lineno}: {exc.msg}")

        if not any(item.startswith(path.name + ":") for item in errors):
            print(f"VALID: {path.name}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(NOTEBOOKS)} notebook(s). Cells were not executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
