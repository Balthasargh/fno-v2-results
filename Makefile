.PHONY: install install-dev install-all analyze plot report dashboard test lint clean docker

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

install-all:
	pip install -e ".[all]"

analyze:
	python scripts/analyze_results.py

plot:
	python scripts/plot_results.py --out-dir outputs

report:
	python scripts/generate_report.py --out outputs/report.html

dashboard:
	streamlit run scripts/dashboard.py

test:
	pytest -q

lint:
	ruff check src scripts tests

clean:
	rm -rf build dist *.egg-info outputs .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

docker:
	docker build -t fno-v2-results .
	docker run --rm fno-v2-results
