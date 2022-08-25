pytest -s -v -m "sanity" .\testCases\ --browser chrom
pytest -s -v -m "sanity" .\testCases\ --browser edg
rem pytest -s -v -m "sanity" and "regression" .\testCases\ --browser chrom
rem pytest -s -v -m "sanity" or "regression" .\testCases\ --browser chrom