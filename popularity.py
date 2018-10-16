

def popularity(movies_metadata):

    # calculating the popularity of movies
    number_of_votes = movies_metadata['vote_count']
    average_rating = movies_metadata['vote_average']
    mean_vote = movies_metadata['vote_average'].mean()
    min_votes = movies_metadata['vote_count'].quantile(0.9)

    weighted_rating = (number_of_votes / (number_of_votes + min_votes) * average_rating) + \
                      (min_votes / (number_of_votes + min_votes) * mean_vote)

    # first we filter movies and throw out the ones that don't have enough votes
    recommended_movies = movies_metadata.copy().loc[movies_metadata['vote_count'] >= min_votes]
    recommended_movies.shape

    # applying calculated rating to popularity column
    recommended_movies['popularity'] = weighted_rating
    # order movies descending by popularity
    recommended_movies = recommended_movies.sort_values('popularity', ascending=False)

    return recommended_movies[['title', 'vote_count', 'vote_average', 'popularity']]
