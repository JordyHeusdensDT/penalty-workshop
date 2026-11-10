---
name: bigquery-cost-guard
description: Keep BigQuery queries cheap. Use before any query on the scouting data (penalty sql or the query_scouting tool).
---
# BigQuery cost guard

Every byte you scan comes out of your budget, and wasted bytes cost points.

1. Look at the table first: `SELECT * FROM scouting.INFORMATION_SCHEMA.COLUMNS` and `...TABLE_OPTIONS` show the columns, the partitioning and the clustering.
2. Never `SELECT *` on a large table. Select only the columns you need.
3. Filter on the partition column with a constant (`WHERE match_date = DATE '...'`), so BigQuery reads one partition, not all of them.
4. Filter on the cluster columns too: BigQuery skips blocks that cannot match.
5. Start with `LIMIT` and a narrow filter, then widen step by step.
6. `LIMIT` alone does not reduce the bytes scanned.
