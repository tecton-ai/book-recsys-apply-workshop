from datetime import timedelta

from feast import FeatureView, Field
from feast.infra.offline_stores.contrib.spark_offline_store.spark_source import (
    SparkSource,
)
from feast.types import String
from entities import user

users_source = SparkSource(
    name="users_source",
    table="book_recsys_apply.users",
    timestamp_field="signup_date",
)

user_features = FeatureView(
    name="user_features",
    entities=[user],
    schema=[
        Field(name="country", dtype=String),
    ],
    ttl=timedelta(days=365 * 3),
    source=users_source,
)
