from tecton import FileConfig, BatchSource

ratings_batch = BatchSource(
    name='ratings_batch',
    batch_config=FileConfig(
        uri="s3://tecton-demo-data/apply-book-recsys/ratings.parquet",
        file_format="parquet",
        timestamp_field='rating_timestamp',
    ),
    owner='jake@tecton.ai',
    tags={'release': 'production'},
    description='User book ratings.'
)