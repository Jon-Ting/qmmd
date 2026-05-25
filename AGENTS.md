# AGENTS.md — AI agent instructions for covdrugsim

Purpose: Help AI coding agents understand project layout, install/test commands, and conventions. Keep this file minimal and link to detailed docs where appropriate.

## Quick facts

- **Python:** >=3.10 (see [pyproject.toml](pyproject.toml#L1-L10)).
- **Source:** code lives under [src/covdrugsim](src/covdrugsim).
- **Tests:** unit tests in [tests/](tests) — run with `uv sync` then `uv run pytest -q` or `python -m pytest tests/`.
- **Build/packaging:** Uses `hatchling` as the build backend (see [pyproject.toml](pyproject.toml#L1-L20)).
- **Entry point:** `covdrugsim` script is defined in `pyproject.toml` -> `covdrugsim.main:main`.

## Useful commands

Run locally (recommended):

```
uv sync
uv run pytest -q
```

Alternative (no uv):

```
python -m pip install -e .
python -m pytest tests/
```

Run linter (ruff configured in `pyproject.toml`):

```
ruff check .
```

Build docs (see `docs/`):

```
# install docs deps (see docs/requirements.txt)
make -C docs html
```

## Agent guidance

- Prefer linking to existing documentation ([README.md](README.md#L1-L20), [CONTRIBUTING.md](CONTRIBUTING.md#L1-L20), `docs/`) instead of copying text.
- Keep changes minimal and focused; do not alter release/version files (e.g., `pyproject.toml:project.version`) without explicit instruction.
- When proposing code changes, include tests or update `tests/` accordingly and run the test suite before suggesting merges.
- When asked to run or modify CI, inspect `.github/workflows/` and reference relevant workflow files.

## Where to look first

- Project metadata and scripts: [pyproject.toml](pyproject.toml#L1-L120)
- Contributor workflow: [CONTRIBUTING.md](CONTRIBUTING.md#L1-L200)
- Documentation and examples: [docs/](docs) and [docs/example.ipynb](docs/example.ipynb)
- Source code entry: [src/covdrugsim/main.py](src/covdrugsim/main.py)

---

If you want a more targeted agent (for tests, release automation, or docs authoring), I can create a dedicated skill or hook. Suggest next: `/create-agent tests` or `/create-skill docs`.
