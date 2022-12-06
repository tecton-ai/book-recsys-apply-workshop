from datetime import timedelta

from feast import FeatureView, Field
from feast.infra.offline_stores.contrib.spark_offline_store.spark_source import (
    SparkSource,
)
from feast.types import Int64, String
from entities import user

users_age_source = SparkSource(
    name="users_age_source",
    table="book_recsys_apply.bucketed_age",
    timestamp_field="signup_date",
)

user_age_features = FeatureView(
    name="user_age_features",
    entities=[user],
    schema=[
        Field(name="bucketedAge", dtype=Int64),
    ],
    ttl=timedelta(days=365 * 3),
    source=users_age_source,
)
