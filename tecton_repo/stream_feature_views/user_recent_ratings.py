from data_sources.ratings_with_book_metadata_stream import ratings_with_book_metadata_stream
import entities
from datetime import datetime, timedelta
from tecton import stream_feature_view, FilteredSource, Aggregation
from tecton.aggregation_functions import last_distinct

@stream_feature_view(
    source=FilteredSource(ratings_with_book_metadata_stream),
    entities=[entities.user],
    mode='pyspark',
    online=True,
    offline=True,
    feature_start_time=datetime(2022, 1, 1),  # Only plan on generating training data from the past year.
    aggregation_interval=timedelta(days=1),
    aggregations=[
        Aggregation(column='rating_summary', function=last_distinct(200), time_window=timedelta(days=365), name='last_200_ratings'),
    ],
    tags={'release': 'production'},
    owner='jake@tecton.ai',
    description='Ratings summaries of the user\'s most recent 200 book ratings.',
)
def user_recent_ratings(ratings_with_book_metadata):
    from pyspark.sql.functions import struct, to_json, col

    df = ratings_with_book_metadata.select(
        col("user_id"),
        col("rating_timestamp"),
        to_json(struct('rating', 'book_author', 'category')).alias("rating_summary")
    )

    return df
