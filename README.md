# Book recommendation system on Tecton

## Data source

- [https://www.kaggle.com/datasets/ruchi798/bookcrossing-dataset](https://www.kaggle.com/datasets/ruchi798/bookcrossing-dataset)
    - note: rating is from 0 to 10
- Add plausible timestamps to all three tables
    - [x]  book timestamps: e.g. base on yearOfPublication + x months
    - [x]  ratings: 2020 - 2023
    - [x]  user signups: 2020 - 2023 (min of random date + min rating for a user)
- See `data_cleaning.ipynb` for cleaning steps

## Cleaned data source
- See files at `s3://tecton-demo-data/apply-book-recsys/`

Files are tracked with DVC too:
- If you have DVC, you can run `dvc pull` to get the data files
- `dvc remote add -d storage s3://tecton-demo-data/apply-book-recsys/`

## Plan
### Where users are today
Often, just getting started (esp with going real-time)

- e.g. Fanduel + LightFM
- e.g. Roblox + complex features, but offline only

### Use case

**- Home page**
- Similar items to this page
- Query / search

## Model approach

**- (first) XGBoost**
- (later) LightFM?
    - does not have concept of user item ratings over time
    - Tecton still adds value though

## Features

- BFV (manage cold start + emulate problem in training)
    - User metadata
        - Locale
        - Age
        - Device type
    - Book metadata
        - Author
        - Category
        - (optional) Description → word2vec?
- LightFM
    - Side features
        - Recent history (SFV + ODFV)
            - (optional) Weighted user embedding of recent history (e.g. pass in embeddings from candidate generation)
            - User favorite categories
                - top 3 in ODFV based on ratings per category
            - Most recent bought category
            - 2nd most recently bought category
            - Average rating by each category
        - ODFV
            - has user read this book category
            - has user read this author
            - month of request
