from datetime import timedelta

from feast import FeatureView, PushSource
from feast.infra.offline_stores.contrib.spark_offline_store.spark_source import (
    SparkSource,
)
from entities import user

user_agg_rating_source = SparkSource(
    name="user_agg_rating_source",
    table="book_recsys_apply.agg_user_features",
    timestamp_field="rating_timestamp",
)

user_agg_rating_features = FeatureView(
    name="user_agg_rating_features",
    entities=[user],
    ttl=timedelta(days=365 * 3),
    source=user_agg_rating_source,
)

user_agg_rating_1d_source = PushSource(
    name="agg_user_features_1d_source",
    batch_source=SparkSource(
        name="agg_user_features_1d",
        table="book_recsys_apply.agg_user_features_1d",
        timestamp_field="rating_timestamp",
        tags={"dbtModel": "demo_dbt/models/example/agg_user_features_1d.sql"},
    ),
)

user_agg_rating_1d_features = FeatureView(
    name="agg_user_features_1d",
    entities=[user],
    ttl=timedelta(days=365 * 3),
    source=user_agg_rating_1d_source,
)
