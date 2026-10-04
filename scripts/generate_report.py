#!/usr/bin/env python3
"""Generate a standalone HTML report from FNO v2 results."""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from fno_v2 import (  # noqa: E402
    load_all,
    rank_models,
    significant_wins,
    mean_nll_by_model,
    summary_report,
)


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>FNO v2 – Rapport d'analyse</title>
  <style>
    :root {{ --bg: #0f172a; --card: #1e293b; --text: #e2e8f0; --accent: #38bdf8; --muted: #94a3b8; }}
    * {{ box-sizing: border-box; }}
    body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 2rem; line-height: 1.5; }}
    h1, h2 {{ color: var(--accent); }}
    .card {{ background: var(--card); border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ padding: 0.5rem 0.75rem; text-align: left; border-bottom: 1px solid #334155; }}
    th {{ color: var(--muted); font-weight: 600; }}
    .badge {{ display: inline-block; background: #0ea5e9; color: #0f172a; padding: 0.15rem 0.5rem; border-radius: 999px; font-size: 0.8rem; font-weight: 600; }}
    pre {{ background: #020617; padding: 1rem; border-radius: 8px; overflow-x: auto; font-size: 0.9rem; }}
    footer {{ color: var(--muted); font-size: 0.85rem; margin-top: 2rem; }}
  </style>
</head>
<body>
  <h1>FNO v2 – Rapport d'analyse</h1>
  <p>Généré le {timestamp} · version package {version}</p>

  <div class="card">
    <h2>Résumé</h2>
    <pre>{summary}</pre>
  </div>

  <div class="card">
    <h2>Classement des modèles (NLL)</h2>
    {ranking_table}
  </div>

  <div class="card">
    <h2>Gains significatifs <span class="badge">FDR < 0.05</span></h2>
    {wins_table}
  </div>

  <div class="card">
    <h2>Prochain tirage</h2>
    {next_draw_table}
  </div>

  <div class="card">
    <h2>Configuration</h2>
    <pre>{config}</pre>
  </div>

  <footer>FNO v2 Results · MIT License</footer>
</body>
</html>
"""


def df_to_html(df) -> str:
    if df is None or (hasattr(df, "empty") and df.empty):
        return "<p><em>Aucune donnée</em></p>"
    return df.to_html(index=False, float_format="%.4f", border=0)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate HTML report")
    parser.add_argument("--data-dir", default=None)
    parser.add_argument("--out", default="outputs/report.html")
    args = parser.parse_args()

    data = load_all(args.data_dir)
    ranked = rank_models(data["models"], "NLL")
    wins = significant_wins(data["comparisons"])
    summary = summary_report(data["models"], data["comparisons"], data["points_test"])

    import json
    from fno_v2 import __version__

    html = HTML_TEMPLATE.format(
        timestamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        version=__version__,
        summary=summary,
        ranking_table=df_to_html(ranked[["rank", "modele", "NLL", "RPS", "top5_hit"]]),
        wins_table=df_to_html(wins[["contre", "metrique", "delta", "p_fdr"]] if not wins.empty else None),
        next_draw_table=df_to_html(data["next_draw"]),
        config=json.dumps(data["config"], indent=2, ensure_ascii=False),
    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"✅ Rapport HTML → {out.resolve()}")


if __name__ == "__main__":
    main()
