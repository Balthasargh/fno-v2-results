#!/usr/bin/env python3
"""Interactive Streamlit dashboard for FNO v2 results."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from fno_v2 import (
    load_all,
    rank_models,
    significant_wins,
    mean_nll_by_model,
    nll_by_fold,
    summary_report,
)


st.set_page_config(page_title="FNO v2 Results", page_icon="📊", layout="wide")
st.title("📊 FNO v2 – Tableau de bord")

data = load_all(ROOT / "results")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Section", ["Résumé", "Modèles", "Comparaisons", "Distributions", "Détails test"])

if page == "Résumé":
    st.subheader("Résumé de l'expérience")
    st.code(summary_report(data["models"], data["comparisons"], data["points_test"]))
    cfg = data["config"]
    c1, c2, c3 = st.columns(3)
    c1.metric("Folds", cfg["config"]["n_folds"])
    c2.metric("Best val NLL", f"{cfg['nll_val_optuna']:.4f}")
    c3.metric("Bagging", "Oui" if cfg["meilleurs_hyperparametres"]["bagging"] else "Non")

elif page == "Modèles":
    st.subheader("Classement des modèles")
    ranked = rank_models(data["models"], "NLL")
    st.dataframe(ranked, use_container_width=True)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(ranked["modele"], ranked["NLL"], color="steelblue")
    ax.set_xlabel("NLL")
    ax.invert_yaxis()
    st.pyplot(fig)

elif page == "Comparaisons":
    st.subheader("Comparaisons statistiques")
    st.dataframe(data["comparisons"], use_container_width=True)
    wins = significant_wins(data["comparisons"])
    st.subheader("Gains significatifs (FDR < 0.05)")
    if wins.empty:
        st.info("Aucun gain significatif.")
    else:
        st.dataframe(wins, use_container_width=True)

elif page == "Distributions":
    st.subheader("Distributions du prochain tirage")
    dists = data["distributions"]
    st.dataframe(data["next_draw"], use_container_width=True)

    fig, axes = plt.subplots(1, 5, figsize=(14, 3), sharey=True)
    for ax, col in zip(axes, dists.index):
        ax.bar(range(1, 51), dists.loc[col].values, width=1.0, color="coral", alpha=0.85)
        ax.set_title(str(col))
        ax.set_xlabel("Valeur")
    axes[0].set_ylabel("Probabilité")
    fig.suptitle("Distributions prédictives", y=1.05)
    plt.tight_layout()
    st.pyplot(fig)

elif page == "Détails test":
    st.subheader("NLL moyen par pli")
    st.dataframe(nll_by_fold(data["points_test"]).round(4), use_container_width=True)
    st.subheader("NLL moyen global")
    st.dataframe(mean_nll_by_model(data["points_test"]).to_frame("mean_NLL"), use_container_width=True)
