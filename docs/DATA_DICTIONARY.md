# Data Dictionary

## `results/config.json`

| Key | Type | Description |
|-----|------|-------------|
| `config.n_folds` | int | Number of CV folds |
| `config.max_epochs` | int | Max training epochs |
| `meilleurs_hyperparametres` | object | Best hyperparameters |
| `nll_val_optuna` | float | Best validation NLL |

## `results/tableau_modeles.csv`

| Column | Description |
|--------|-------------|
| `modele` | Model name |
| `NLL` | Negative log-likelihood |
| `RPS` | Ranked Probability Score |
| `top5_hit` | Top-5 hit rate |

## `results/comparaisons.csv`

| Column | Description |
|--------|-------------|
| `contre` | Baseline model |
| `metrique` | `nll` or `rps` |
| `delta` | FNO − baseline |
| `p_fdr` | FDR-corrected p-value |

## `results/points_test.csv`

Per-observation NLL on the test set (`pli`, `colonne`, `t`, `reel`, `nll_*`).

## `results/prochain_tirage*.csv`

Next-draw summary stats and full discrete distributions over 1…50.
