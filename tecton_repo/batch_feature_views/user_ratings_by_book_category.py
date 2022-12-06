from data_sources.ratings_batch import ratings_batch
from data_sources.books_batch import books_batch
import entities
from tecton import batch_feature_view, Aggregation, FilteredSource
from datetime import datetime, timedelta
from functools import reduce

TOP_10_CATEGORIES = {
    'Fiction': 'fiction',
    'Juvenile Fiction': 'juvenile_fiction',
    'Biography & Autobiography': 'biography',
    'Religion': 'religion',
    'History': 'history',
    'Juvenile Nonfiction': 'juvenile_nonfiction',
    'Social Science': 'social_science',
    'Business & Economics': 'business_and_economics',
    'Body, Mind & Spirit': 'body_mind_and_spirit',
    'Health & Fitness': 'health_and_fitness',
}

aggregations = [
    [
        Aggregation(column=f'{category}_rating', function='mean', time_window=timedelta(days=365), name=f'{category}_rating_mean'),
        Aggregation(column=f'{category}_rating', function='count', time_window=timedelta(days=365), name=f'{category}_rating_count'),
        Aggregation(column=f'{category}_rating', function='stddev_pop', time_window=timedelta(days=365), name=f'{category}_rating_stddev'),
    ]
    for category in TOP_10_CATEGORIES.values()
]

# Flatten the `aggregations` list of lists.
aggregations = reduce(lambda l, r: l + r, aggregations)

# Add the "overall" category.
aggregations = [
    Aggregation(column=f'rating', function='mean', time_window=timedelta(days=365), name=f'overall_rating_mean'),
    Aggregation(column=f'rating', function='count', time_window=timedelta(days=365), name=f'overall_rating_count'),
    Aggregation(column=f'rating', function='stddev_pop', time_window=timedelta(days=365), name=f'overall_rating_stddev'),
] + aggregations

# This feature view produces aggregate metrics for each book category in a user's rating history, e.g. the users average
# rating in the "history" category. This feature view creates three aggregate features for each
# of the top 10 categories plus the "overall" category for a total of 33 features.
#
# An equivalent feature view can be implemented in spark SQL using the PIVOT clause.
@batch_feature_view(
    sources=[FilteredSource(ratings_batch), books_batch],
    entities=[entities.user],
    mode='pyspark',
    online=True,
    offline=True,
    aggregation_interval=timedelta(days=1),
    aggregations=aggregations,
    feature_start_time=datetime(2022, 1, 1),  # Only plan on generating training data from the past year.
    tags={'release': 'production'},
    owner='jake@tecton.ai',
    description='User book rating aggregate metrics split by book category.'
)
def user_ratings_by_book_category(ratings, books):
    from pyspark.sql.functions import col, when

    df = ratings.join(books, ["isbn"], "left")

    for raw_name, clean_name in TOP_10_CATEGORIES.items():
        df = df.withColumn(f'{clean_name}_rating', when(col('category') == raw_name, col('rating')).otherwise(None))

    final_columns = ['user_id', 'rating_timestamp', 'rating'] + [f'{clean_name}_rating' for clean_name in TOP_10_CATEGORIES.values()]
    df = df.select(*final_columns)
    return df
