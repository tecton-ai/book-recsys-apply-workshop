from tecton import FileConfig, BatchSource

books_batch = BatchSource(
    name='books_batch',
    batch_config=FileConfig(
        uri="s3://tecton-demo-data/apply-book-recsys/books_v3.parquet",
        file_format="parquet",
    ),
    owner='jake@tecton.ai',
    tags={'release': 'production'},
    description='Book metadata, e.g. the book title, author, category, language, etc.'
)