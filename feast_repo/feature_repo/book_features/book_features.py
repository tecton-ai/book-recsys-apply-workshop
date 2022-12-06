from datetime import timedelta

from feast import FeatureView, Field
from feast.infra.offline_stores.contrib.spark_offline_store.spark_source import (
    SparkSource,
)
from feast.types import String
from entities import book

# root
#  |-- isbn: string (nullable = true)
#  |-- book_title: string (nullable = true)
#  |-- book_author: string (nullable = true)
#  |-- year_of_publication: integer (nullable = true)
#  |-- publisher: string (nullable = true)
#  |-- Summary: string (nullable = true)
#  |-- Language: string (nullable = true)
#  |-- Category: string (nullable = true)
#  |-- created_at: timestamp (nullable = true)
#  |-- __index_level_0__: long (nullable = true)
books_source = SparkSource(
    name="books_source",
    table="book_recsys_apply.books",
    timestamp_field="created_at",
)

book_features = FeatureView(
    name="book_features",
    entities=[book],
    schema=[
        Field(name="Language", dtype=String),
        Field(name="Category", dtype=String),
    ],
    ttl=timedelta(days=365 * 150),
    source=books_source,
)
