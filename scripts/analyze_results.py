#!/usr/bin/env python3
"""
Script d'analyse des résultats FNO v2.
Usage:
    python scripts/analyze_results.py [--data-dir PATH]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.loader import load_all
from src.analysis import rank_models, significant_wins, mean_nll_by_model


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyse des résultats FNO v2")
    parser.add_argument("--data-dir", type=str, default=None, help="Chemin vers le dossier results/")
    args = parser.parse_args()

    data = load_all(args.data_dir)

    print("=" * 60)
    print("CONFIGURATION")
    print("=" * 60)
    cfg = data["config"]
    print(f"  Folds          : {cfg['config']['n_folds']}")
    print(f"  Best NLL val   : {cfg['nll_val_optuna']:.4f}")
    hp = cfg["meilleurs_hyperparametres"]
    print(f"  Architecture   : L={hp['L']}, modes={hp['modes']}, width={hp['width']}")
    print(f"  LR / WD        : {hp['lr']:.6f} / {hp['wd']:.2e}")
    print(f"  Bagging        : {hp['bagging']}")

    print("\n" + "=" * 60)
    print("CLASSEMENT DES MODÈLES (par NLL)")
    print("=" * 60)
    ranked = rank_models(data["models"], metric="NLL")
    print(ranked[["rank", "modele", "NLL", "RPS", "top5_hit"]].to_string(index=False))

    print("\n" + "=" * 60)
    print("GAINS SIGNIFICATIFS (p_fdr < 0.05, delta < 0)")
    print("=" * 60)
    wins = significant_wins(data["comparisons"])
    if wins.empty:
        print("  Aucun gain significatif détecté.")
    else:
        print(wins[["contre", "metrique", "delta", "p_fdr"]].to_string(index=False))

    print("\n" + "=" * 60)
    print("NLL MOYEN SUR LE JEU DE TEST")
    print("=" * 60)
    mean_nll = mean_nll_by_model(data["points_test"])
    for model, val in mean_nll.items():
        print(f"  {model:<30} {val:.4f}")

    print("\n" + "=" * 60)
    print("PROCHAIN TIRAGE (résumé)")
    print("=" * 60)
    print(data["next_draw"].to_string(index=False))

    print("\n✅ Analyse terminée.")


if __name__ == "__main__":
    main()
