{{ 
  config(
    materialized='incremental',
    file_format='parquet',
    incremental_strategy='append'
  ) 
}}

SELECT
  user_id,
  signup_date,
  CASE 
    WHEN age < 0 THEN -1
    WHEN age >= 0 AND age <= 10 THEN 0
    WHEN age > 10 AND age <= 20 THEN 1
    WHEN age > 20 AND age <= 30 THEN 2
    WHEN age > 30 AND age <= 40 THEN 3
    WHEN age > 40 AND age <= 50 THEN 4
    WHEN age > 50 AND age <= 60 THEN 5
    WHEN age > 60 AND age <= 70 THEN 6
    WHEN age > 70 AND age <= 80 THEN 7
    WHEN age > 80 AND age <= 90 THEN 8
    WHEN age > 90 AND age <= 100 THEN 9
    ELSE 10 
  END AS bucketedAge
FROM
  book_recsys_apply.users
{% if is_incremental() %}
WHERE
  signup_date 
    BETWEEN 
      (SELECT MAX(signup_date)::date FROM {{ this}}) AND 
      (SELECT date_add(MAX(signup_date)::date, 1) FROM {{ this}})
{% endif %}
