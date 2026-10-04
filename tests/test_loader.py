"""Basic tests for the FNO v2 loader."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from fno_v2 import (
    load_all,
    load_config,
    load_models_table,
    load_comparisons,
    load_points_test,
    load_next_draw,
    load_distributions,
)

DATA = Path(__file__).resolve().parent.parent / "results"


def test_load_config():
    cfg = load_config(DATA)
    assert "config" in cfg
    assert "meilleurs_hyperparametres" in cfg
    assert cfg["config"]["n_folds"] == 3


def test_load_models_table():
    df = load_models_table(DATA)
    assert isinstance(df, pd.DataFrame)
    assert "modele" in df.columns
    assert "NLL" in df.columns
    assert len(df) >= 5


def test_load_comparisons():
    df = load_comparisons(DATA)
    assert "contre" in df.columns
    assert "p_fdr" in df.columns


def test_load_points_test():
    df = load_points_test(DATA)
    assert "pli" in df.columns
    assert len(df) == 75


def test_load_next_draw():
    df = load_next_draw(DATA)
    assert "esperance" in df.columns
    assert len(df) == 5


def test_load_distributions():
    df = load_distributions(DATA)
    assert df.shape[0] == 5
    assert df.shape[1] == 50


def test_load_all():
    data = load_all(DATA)
    assert set(data.keys()) == {
        "config",
        "models",
        "comparisons",
        "points_test",
        "next_draw",
        "distributions",
    }
