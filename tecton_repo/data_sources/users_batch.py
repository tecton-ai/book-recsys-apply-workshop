from tecton import FileConfig, BatchSource

users_batch = BatchSource(
    name='users_batch',
    batch_config=FileConfig(
        uri="s3://tecton-demo-data/apply-book-recsys/users.parquet",
        file_format="parquet",
    ),
    owner='jake@tecton.ai',
    tags={'release': 'production'},
    description='User metadata, e.g. their sign-up date, age, and location.'
)