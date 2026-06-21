import pandas as pd


df =pd.read_csv('archive/netflix_titles.csv')


content_per_year = (
    df.groupby("release_year")
      .size()
      .reset_index(name="count")
      .sort_values("release_year")
).head(51)

content_per_year.to_csv("result/content_per_year.csv", index= False)


# Dominant countries
countries = (
    df["country"]
    .dropna()
    .str.split(", ")
    .explode()
)

top_countries = countries.value_counts().head(10)

top_countries.to_csv("result/top_countries.csv", index= False)


# Type count
type_counts = df["type"].value_counts()
type_counts.to_csv("result/type_counts.csv", index= False)


# Top genres
genres = (
    df["listed_in"]
    .str.split(", ")
    .explode()
)

top_genres = genres.value_counts().head(15)
top_genres.to_csv("result/top_genres.csv", index= False)


# Dominant rating
rating_counts = df["rating"].value_counts()
rating_counts.to_csv("result/rating_counts.csv", index= False)







