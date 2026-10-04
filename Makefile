.PHONY: install install-dev analyze plot test lint clean

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

analyze:
	python scripts/analyze_results.py

plot:
	python scripts/plot_results.py --out-dir outputs

test:
	pytest -q

lint:
	ruff check src scripts tests

clean:
	rm -rf build dist *.egg-info outputs .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
