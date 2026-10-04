# FNO v2 Results

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Analysis toolkit and experimental results** for a Fourier Neural Operator (FNO) v2 study.

## Features

- Model ranking (NLL, RPS, MAE, top-5 hit rate)
- Statistical comparisons vs strong baselines (ARIMA, LightGBM, GRU, LSTM…)
- Next-draw probability distributions
- Installable Python package with typed helpers
- Simple CLI (`analyze` / `plot`)

## Project structure

```
fno-v2-results/
├── pyproject.toml
├── requirements.txt
├── Makefile
├── LICENSE
├── results/                 # Experimental data
├── images/                  # Figures (PNG)
├── src/fno_v2/              # Python package
│   ├── loader.py
│   └── analysis.py
├── scripts/
│   ├── analyze_results.py
│   └── plot_results.py
└── tests/
```

## Installation

```bash
git clone https://github.com/Balthasargh/fno-v2-results.git
cd fno-v2-results
pip install -e .
# or with dev tools:
pip install -e ".[dev]"
```

## Quick start

```bash
make analyze          # text analysis
make plot             # generate plots → outputs/
make test             # run unit tests
```

## Python API

```python
from fno_v2 import load_all, rank_models, significant_wins, mean_nll_by_model

data = load_all()
print(rank_models(data["models"]))
print(significant_wins(data["comparisons"]))
print(mean_nll_by_model(data["points_test"]))
```

## Main results

| Model                 | NLL   | RPS   | top5_hit |
|-----------------------|-------|-------|----------|
| Uniforme              | 3.912 | 0.175 | 0.12     |
| **FNO global (ens.)** | 3.915 | 0.176 | 0.07     |
| GRU                   | 3.993 | 0.196 | 0.08     |
| LSTM                  | 4.038 | 0.201 | 0.11     |
| LightGBM              | 4.223 | 0.198 | 0.03     |

Best hyperparameters (Optuna): `L=4`, `modes=3`, `width=24`, bagging enabled.  
Validation NLL ≈ 3.810.

## Development

```bash
make install-dev
make test
make lint
make clean
```

## License

MIT – see [LICENSE](LICENSE).
