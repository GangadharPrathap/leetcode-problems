WITH data_per_day AS (
  SELECT
    visited_on AS visit_date,
    SUM(amount) AS total_amount
  FROM
    customer
  GROUP BY
    visited_on
),
req_data AS (
  SELECT
    visit_date,
    SUM(total_amount) OVER (ORDER BY visit_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS running_total,
    ROUND(SUM(total_amount) OVER (ORDER BY visit_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) / 7, 2) AS average_daily_amount,
    ROW_NUMBER() OVER (ORDER BY visit_date) AS row_num
  FROM
    data_per_day
)
SELECT
  TO_CHAR(visit_date, 'YYYY-MM-DD') AS visited_on,
  running_total AS amount,
  average_daily_amount AS average_amount
FROM
  req_data
WHERE
  row_num > 6;