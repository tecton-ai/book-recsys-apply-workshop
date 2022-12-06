from feast import FeatureService

from book_features.book_agg_rating_features import book_agg_rating_features
from book_features.book_features import book_features
from book_features.book_category_agg_features import avg_book_category_rating_features
from user_features.user_agg_rating_features import (
    user_agg_rating_features,
    user_agg_rating_1d_features,
)
from user_features.user_age_features import user_age_features
from user_features.user_features import user_features

model_v1 = FeatureService(
    name="model_v1",
    features=[book_features, user_features, user_age_features],
)

model_v2 = FeatureService(
    name="model_v2",
    features=[
        book_features,
        user_features,
        user_age_features,
        book_agg_rating_features,
    ],
)

model_v3 = FeatureService(
    name="model_v3",
    features=[
        book_features,
        user_features,
        user_age_features,
        book_agg_rating_features,
        user_agg_rating_features,
    ],
)

model_v4 = FeatureService(
    name="model_v4",
    features=[
        book_features,
        user_features,
        book_agg_rating_features,
        user_agg_rating_features,
        user_agg_rating_1d_features,
        avg_book_category_rating_features,
    ],
)
