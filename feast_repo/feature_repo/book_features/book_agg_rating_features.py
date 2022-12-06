from datetime import timedelta

from feast import FeatureView
from feast.infra.offline_stores.contrib.spark_offline_store.spark_source import (
    SparkSource,
)
from entities import book

book_agg_ratings_source = SparkSource(
    name="book_agg_ratings_source",
    table="book_recsys_apply.agg_book_features",
    timestamp_field="rating_timestamp",
)

book_agg_rating_features = FeatureView(
    name="book_agg_rating_features",
    entities=[book],
    ttl=timedelta(days=365 * 150),
    source=book_agg_ratings_source,
)
