# FNO v2 Results

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-green.svg)](.github/workflows/ci.yml)

**Analysis toolkit and experimental results** for a Fourier Neural Operator (FNO) v2 study.

## Features

- Model ranking & statistical comparisons
- Next-draw probability distributions
- Installable package + typed API
- CLI, Jupyter notebook & **Streamlit dashboard**
- Standalone **HTML report**
- Docker support
- Unit tests + GitHub Actions CI

## Quick start (all OS)

```bash
git clone https://github.com/Balthasargh/fno-v2-results.git
cd fno-v2-results

python -m venv .venv
# Linux/macOS:  source .venv/bin/activate
# Windows:      .venv\Scripts\activate

pip install -e ".[all]"

make analyze      # or: python scripts/analyze_results.py
make plot         # or: python scripts/plot_results.py
make report       # HTML → outputs/report.html
make dashboard    # Streamlit UI
make test
```

## Python API

```python
from fno_v2 import load_all, rank_models, significant_wins, summary_report

data = load_all()
print(summary_report(data["models"], data["comparisons"], data["points_test"]))
print(rank_models(data["models"]))
```

## Project structure

```
├── results/           # Experimental data
├── images/            # Figures
├── src/fno_v2/        # Package
├── scripts/           # CLI, report, dashboard
├── notebooks/         # Exploration notebook
├── tests/
├── docs/              # Data dictionary
├── Dockerfile
└── .github/workflows/ # CI
```

## Main results

| Model                 | NLL   | RPS   | top5_hit |
|-----------------------|-------|-------|----------|
| Uniforme              | 3.912 | 0.175 | 0.12     |
| **FNO global (ens.)** | 3.915 | 0.176 | 0.07     |
| GRU                   | 3.993 | 0.196 | 0.08     |
| LSTM                  | 4.038 | 0.201 | 0.11     |
| LightGBM              | 4.223 | 0.198 | 0.03     |

Best hyperparameters (Optuna): `L=4`, `modes=3`, `width=24`, bagging.  
Validation NLL ≈ 3.810.

## Docker

```bash
docker build -t fno-v2-results .
docker run --rm fno-v2-results
```

## License

MIT – see [LICENSE](LICENSE).
