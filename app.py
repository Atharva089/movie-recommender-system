# import pickle
# from typing import List, Any
# from urllib import response
# import requests
# import streamlit as st
# import pandas as pd
#
# st.title('Movie Recommender System')
#
# #this will unload the data from the .pkl file into the movie_dict var
# movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movie_dict)        #create a new data frame
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# selected_movie_name = st.selectbox(
#     'Look for your favorite movies here 🍿',
#     movies['title'].values)
#
# #takes a movie as input and recommends 5 more similar movies
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     #empty list which will store the (five) recommended movies
#     recommend_movies: list[Any] = []
#     recommend_movies_poster = []
#
#     for i in movie_list:
#         movie_id = i[movies.iloc[i[0]].movie_id]
#         recommend_movies.append(movies.iloc[i[0]].title)  #movies will be appended in the empty list
#         recommend_movies_poster.append(fetch_poster(movie_id))
#
#     return recommend_movies, recommend_movies_poster
#
# def fetch_poster(movie_id):
#     requests.get('https://api.themoviedb.org/3/movie{}?api_key=e6c9554171b82ef5d5c5ac8782f14c27&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#
#
# if st.button("Recommend"):
#     names, posters = recommend(selected_movie_name)
#
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.header(names[0])
#         st.image(posters[0])
#
#     with col2:
#         st.header(names[1])
#         st.image(posters[1])
#
#     with col3:
#         st.header(names[2])
#         st.image(posters[2])
#
#     with col4:
#         st.header(names[3])
#         st.image(posters[3])
#
#     with col5:
#         st.header(names[4])
#         st.image(posters[4])
#
#

import pickle
from typing import List, Any
import requests
import streamlit as st
import pandas as pd

st.title('Movie Recommender System')

# This will unload the data from the .pkl file into the movie_dict var
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)  # Create a new data frame
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    'Look for your favorite movies here 🍿',
    movies['title'].values)

# Takes a movie as input and recommends 5 more similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Empty list which will store the (five) recommended movies
    recommend_movies = []
    recommend_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)  # Movies will be appended in the empty list
        recommend_movies_poster.append(fetch_poster(movie_id))

    return recommend_movies, recommend_movies_poster

# def fetch_poster(movie_id):
#     url = 'https://api.themoviedb.org/3/movie/{}?api_key=e6c9554171b82ef5d5c5ac8782f14c27&language=en-US'.format(movie_id)
#     response = requests.get(url)
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=e6c9554171b82ef5d5c5ac8782f14c27&language=en-US'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750.png?text=Poster+Not+Available"
    else:
        return "https://via.placeholder.com/500x750.png?text=API+Error"



if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        # st.header(names[0])
        st.image(posters[0])
        st.markdown(names[0])

    with col2:
        # st.header(names[1])
        st.image(posters[1])
        st.markdown(names[1])

    with col3:
        # st.header(names[2])
        st.image(posters[2])
        st.markdown(names[2])

    with col4:
        # st.header(names[3])
        st.image(posters[3])
        st.markdown(names[3])

    with col5:
        # st.header(names[4])
        # st.caption(names[4])
        st.image(posters[4])
        st.markdown(names[4])

