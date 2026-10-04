# FNO v2 Results

Résultats de l'expérimentation **Fourier Neural Operator (FNO) v2**.

## Structure

```
fno-v2-results/
├── README.md
├── results/
│   ├── config.json                      # Hyperparamètres et configuration
│   ├── tableau_modeles.csv              # Comparaison des modèles (NLL, RPS, MAE...)
│   ├── comparaisons.csv                 # Tests statistiques (delta, p-values)
│   ├── points_test.csv                  # Prédictions point par point (test set)
│   ├── prochain_tirage.csv              # Statistiques du prochain tirage
│   └── prochain_tirage_distributions.csv # Distributions de probabilité
└── docs/                                # (optionnel) figures et analyses
```

## Contenu principal

### `config.json`
Configuration de l'expérience et meilleurs hyperparamètres trouvés par Optuna :
- Architecture FNO (`L`, `modes`, `width`, ...)
- Optimisation (`lr`, `wd`, `sigma`, bagging...)
- NLL de validation

### `tableau_modeles.csv`
Classement des modèles sur le set de test (NLL, RPS, MAE médiane/moyenne, top-5 hit rate).

### `comparaisons.csv`
Comparaisons statistiques vs baselines (Uniforme, Marginale empirique, AR(1), ARIMA, LightGBM, GRU, LSTM).

### `points_test.csv`
NLL de chaque modèle pour chaque observation du jeu de test (pli, colonne, temps, valeur réelle).

### `prochain_tirage.csv` & `prochain_tirage_distributions.csv`
Prédiction du prochain tirage (espérance, médiane, top-5, distributions complètes par colonne).

## Utilisation

```python
import pandas as pd
import json

# Config
with open("results/config.json") as f:
    config = json.load(f)

# Tableaux
models = pd.read_csv("results/tableau_modeles.csv")
comparisons = pd.read_csv("results/comparaisons.csv")
points = pd.read_csv("results/points_test.csv")
next_draw = pd.read_csv("results/prochain_tirage.csv")
dists = pd.read_csv("results/prochain_tirage_distributions.csv", index_col=0)
```

## Licence

MIT
