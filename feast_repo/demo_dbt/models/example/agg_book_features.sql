{{ 
  config(
    materialized='incremental',
    file_format='parquet',
    incremental_strategy='append'
  ) 
}}

SELECT
  isbn,
  rating_timestamp,
  AVG(rating) OVER (
    PARTITION BY isbn
    ORDER BY rating_timestamp
    RANGE BETWEEN INTERVAL 365 day PRECEDING AND CURRENT ROW
  ) AS avg_yr_book_rating,
  COUNT(rating) OVER (
    PARTITION BY isbn
    ORDER BY rating_timestamp
    RANGE BETWEEN INTERVAL 365 day PRECEDING AND CURRENT ROW
  ) AS count_yr_book_rating
FROM book_recsys_apply.ratings
{% if is_incremental() %}
WHERE
  rating_timestamp 
    BETWEEN 
      (SELECT date_add(MAX(rating_timestamp)::date, -364) FROM {{ this }}) AND 
      (SELECT date_add(MAX(rating_timestamp)::date, 1) FROM {{ this }})
{% endif %}
