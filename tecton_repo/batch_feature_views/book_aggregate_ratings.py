import entities
from datetime import datetime, timedelta
from data_sources.ratings_batch import ratings_batch
from tecton import batch_feature_view, FilteredSource, Aggregation

@batch_feature_view(
    sources=[FilteredSource(ratings_batch)],
    entities=[entities.book],
    mode='spark_sql',
    online=True,
    offline=True,
    feature_start_time=datetime(2022, 1, 1),  # Only plan on generating training data from the past year.
    aggregation_interval=timedelta(days=1),
    aggregations=[
        Aggregation(column='rating', function='mean', time_window=timedelta(days=365)),
        Aggregation(column='rating', function='mean', time_window=timedelta(days=30)),
        Aggregation(column='rating', function='stddev', time_window=timedelta(days=365)),
        Aggregation(column='rating', function='stddev', time_window=timedelta(days=30)),
        Aggregation(column='rating', function='count', time_window=timedelta(days=365)),
        Aggregation(column='rating', function='count', time_window=timedelta(days=30)),
    ],
    tags={'release': 'production'},
    owner='jake@tecton.ai',
    description='Book aggregate rating features over the past year and past 30 days.',
)
def book_aggregate_ratings(ratings):
    return f'''
        SELECT
            isbn,
            rating_timestamp,
            rating
        FROM
            {ratings}
        '''
