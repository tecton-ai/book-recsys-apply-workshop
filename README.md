# [Public] Book recommendation system on Tecton

## Data source

- Inspired by [https://www.kaggle.com/datasets/ruchi798/bookcrossing-dataset](https://www.kaggle.com/datasets/ruchi798/bookcrossing-dataset)
    - note: rating is from 0 to 10
- Add plausible timestamps to all three tables
    - [x]  book timestamps: e.g. base on yearOfPublication + x months
    - [x]  ratings: 2020 - 2023
    - [x]  user signups: 2020 - 2023 (min of random date + min rating for a user)
- See `data_cleaning.ipynb` for cleaning steps

## Cleaned data source
See files at [`s3://tecton-demo-data/apply-book-recsys/`](https://s3.console.aws.amazon.com/s3/buckets/tecton-demo-data?region=us-west-2&prefix=apply-book-recsys/&showversions=false)

Files are tracked with DVC too:
- If you have DVC, you can run `dvc pull` to get the data files

### (optional) DVC
- `dvc init`
- `dvc add books_data/`
- `dvc remote add -d storage s3://tecton-demo-data/apply-book-recsys/`
- `dvc push`
