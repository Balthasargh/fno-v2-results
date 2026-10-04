# FNO v2 Results

Résultats de l'expérimentation **Fourier Neural Operator (FNO) v2** + outils d'analyse Python.

## Structure

```
fno-v2-results/
├── README.md
├── LICENSE
├── requirements.txt
├── results/                          # Données de l'expérience
│   ├── config.json
│   ├── tableau_modeles.csv
│   ├── comparaisons.csv
│   ├── points_test.csv
│   ├── prochain_tirage.csv
│   └── prochain_tirage_distributions.csv
├── images/                           # Figures (PNG)
├── docs/                             # Documentation / figures
├── src/
│   ├── __init__.py
│   ├── loader.py
│   └── analysis.py
└── scripts/
    ├── analyze_results.py
    └── plot_results.py
```

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
# Analyse textuelle
python scripts/analyze_results.py

# Graphiques
python scripts/plot_results.py --out-dir outputs
```

## Exemple de code

```python
from src.loader import load_all
from src.analysis import rank_models, significant_wins

data = load_all()
print(rank_models(data["models"]))
print(significant_wins(data["comparisons"]))
```

## Contenu des résultats

| Fichier | Description |
|---------|-------------|
| `config.json` | Hyperparamètres Optuna + config expérience |
| `tableau_modeles.csv` | Classement des modèles (NLL, RPS, MAE, top5) |
| `comparaisons.csv` | Tests statistiques vs baselines |
| `points_test.csv` | NLL point par point sur le test set |
| `prochain_tirage.csv` | Stats du prochain tirage |
| `prochain_tirage_distributions.csv` | Distributions complètes |

## Licence

MIT
