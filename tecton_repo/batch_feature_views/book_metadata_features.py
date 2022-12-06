from data_sources.books_batch import books_batch
import entities
from datetime import datetime, timedelta
from tecton import batch_feature_view


@batch_feature_view(
    sources=[books_batch],
    entities=[entities.book],
    mode='spark_sql',
    online=True,
    offline=True,
    feature_start_time=datetime(2018, 1, 1),  # First book metadata row `created_at` date.
    batch_schedule=timedelta(days=1),
    ttl=timedelta(days=365 * 10),
    tags={'release': 'production'},
    owner='jake@tecton.ai',
    description='Book metadata features.',
)
def book_metadata_features(books):
    return f'''
        SELECT
            isbn,
            created_at,
            book_title,
            book_author,
            year_of_publication,
            category
        FROM
            {books}
        '''
