from data_sources.users_batch import users_batch
import entities
from datetime import datetime, timedelta
from tecton import batch_feature_view


@batch_feature_view(
    sources=[users_batch],
    entities=[entities.user],
    mode='spark_sql',
    online=True,
    offline=True,
    feature_start_time=datetime(2020, 1, 1),  # First user sign-up date.
    batch_schedule=timedelta(days=1),
    ttl=timedelta(days=365 * 10),
    tags={'release': 'production'},
    owner='jake@tecton.ai',
    description='Book metadata features.',
)
def user_demographic_features(users):
    return f'''
        SELECT
            user_id,
            signup_date,
            age,
            country
        FROM
            {users}
        '''
