#!/usr/bin/env python3
"""
Génère des graphiques à partir des résultats FNO v2.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.loader import load_all


def plot_model_ranking(models: pd.DataFrame, out: Path) -> None:
    df = models.sort_values("NLL")
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(df["modele"], df["NLL"], color="steelblue")
    ax.set_xlabel("NLL (plus bas = meilleur)")
    ax.set_title("Classement des modèles – NLL")
    ax.invert_yaxis()
    for bar, val in zip(bars, df["NLL"]):
        ax.text(val + 0.005, bar.get_y() + bar.get_height() / 2, f"{val:.3f}", va="center", fontsize=8)
    fig.tight_layout()
    fig.savefig(out / "ranking_nll.png", dpi=150)
    plt.close()


def plot_distributions(dists: pd.DataFrame, out: Path) -> None:
    fig, axes = plt.subplots(1, 5, figsize=(16, 3.5), sharey=True)
    values = np.arange(1, dists.shape[1] + 1)
    for i, (ax, col) in enumerate(zip(axes, dists.index)):
        ax.bar(values, dists.loc[col].values, width=1.0, color="coral", alpha=0.85)
        ax.set_title(col)
        ax.set_xlabel("Valeur")
        if i == 0:
            ax.set_ylabel("Probabilité")
    fig.suptitle("Distributions du prochain tirage", y=1.02)
    fig.tight_layout()
    fig.savefig(out / "distributions.png", dpi=150, bbox_inches="tight")
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default=None)
    parser.add_argument("--out-dir", default="outputs")
    args = parser.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    data = load_all(args.data_dir)
    plot_model_ranking(data["models"], out)
    plot_distributions(data["distributions"], out)
    print(f"✅ Graphiques sauvegardés dans {out.resolve()}")


if __name__ == "__main__":
    main()
