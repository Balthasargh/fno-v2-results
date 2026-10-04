# Results data

Most CSV files are complete in this repository.

If `points_test.csv` appears truncated (should be **75 data rows**),
replace it with the full file from the release archive or from:

```bash
# From the professional zip
cp fno_v2_pro/results/points_test.csv results/
cp fno_v2_pro/images/*.png images/
git add results/points_test.csv images/
git commit -m "Add complete points_test.csv and images"
git push
```

Expected sizes:
- `points_test.csv` ≈ 11.8 KB (76 lines)
- `prochain_tirage_distributions.csv` ≈ 5.3 KB (6 lines) ✅ complete
- `images/evaluation.png`, `images/prochain_tirage.png`
