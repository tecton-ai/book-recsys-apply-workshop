from datetime import timedelta

from feast import FeatureView
from feast.infra.offline_stores.contrib.spark_offline_store.spark_source import (
    SparkSource,
)
from entities import book

avg_book_category_rating_source = SparkSource(
    name="avg_book_category_rating_source",
    table="book_recsys_apply.avg_book_category_ratings",
    timestamp_field="rating_timestamp",
)

avg_book_category_rating_features = FeatureView(
    name="avg_book_category_rating_features",
    entities=[book],
    ttl=timedelta(days=365 * 3),
    source=avg_book_category_rating_source,
)
