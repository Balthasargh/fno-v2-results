# Contributing

Thanks for your interest in improving this project.

## Development setup

```bash
git clone https://github.com/Balthasargh/fno-v2-results.git
cd fno-v2-results
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Guidelines

1. **Code style** – follow `ruff` (line length 100).
2. **Tests** – add or update tests in `tests/` for new features.
3. **Commits** – use clear, descriptive messages.
4. **Pull requests** – keep them focused; CI must pass.

## Running checks locally

```bash
make lint
make test
make analyze
```

## Reporting issues

Open an issue with a clear description, steps to reproduce, Python version and OS.
