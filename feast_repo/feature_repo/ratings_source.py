from feast.infra.offline_stores.contrib.spark_offline_store.spark_source import (
    SparkSource,
)

ratings_source = SparkSource(
    name="ratings_source",
    file_format="parquet",
    path="s3://tecton-demo-data/apply-book-recsys/ratings.parquet",
    timestamp_field="rating_timestamp",
)
