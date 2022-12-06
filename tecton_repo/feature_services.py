from tecton import FeatureService
from batch_feature_views.book_aggregate_ratings import book_aggregate_ratings
from batch_feature_views.book_metadata_features import book_metadata_features
from batch_feature_views.user_demographic_features import user_demographic_features
from batch_feature_views.user_ratings_by_book_category import user_ratings_by_book_category
from on_demand_feature_views.user_ratings_similar_to_candidate_book import user_ratings_similar_to_candidate_book

book_recsys_feature_service = FeatureService(
    name='book_recsys_feature_service',
    online_serving_enabled=False,
    features=[
        book_aggregate_ratings,
        book_metadata_features[["category", "year_of_publication", "book_author"]],
        user_demographic_features,
        user_ratings_by_book_category,
        user_ratings_similar_to_candidate_book
    ]
)