import pandas as pd
import matplotlib.pyplot as plt

ratings = pd.read_csv(r'E:\6th August 2017 Python - Afternoon\day16\ml-100kC\u.data',
                      sep='\t', names=['userId', 'movieId', 'rating', 'timestamp'])
ratings.groupby('movieId').size().sort_values(ascending=False).head(5)

movie = pd.read_csv(r'E:\6th August 2017 Python - Afternoon\day16\ml-100k\u.item',
                    sep='|', names=['movieId', 'movieName'], usecols=[0,1])

users = pd.read_csv(r'E:\6th August 2017 Python - Afternoon\day16\ml-100k\u.user',
                    sep='|', names=['userId', 'age', 'gender', 'occupation', 'pincode'])

movie_ratings = pd.merge(movie, ratings, on='movieId')
movie_ratings_users = pd.merge(movie_ratings, users, on='userId')
movie_ratings_users.groupby('age').size().sort_values(ascending=False).head(5)
movie_ratings_users['age-group'] = pd.cut(movie_ratings_users['age'],range(0, 81, 10),right=False, labels=['0-9', '10-19', '20-29', '30-39','40-49', '50-59', '60-69', '70-79'])
print (movie_ratings_users[movie_ratings_users['occupation'] == 'student'].groupby(['age-group', 'occupation']).size().sort_values(ascending=False).head(5))
