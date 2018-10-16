import pandas as pd
from popularity import popularity

# Reading a csv into Pandas data frame.
movies_metadata = pd.read_csv('movie_data/movies_metadata.csv', header=0, low_memory=False)

# calling function popularity
recommended_movies = popularity(movies_metadata)

# test printing
print(recommended_movies.head(10))

