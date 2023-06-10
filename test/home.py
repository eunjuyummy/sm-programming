import streamlit as st
import pandas as pd

# Assuming you have the recommended_movies DataFrame
# Read the movie data
movie_df = pd.read_csv('test/movie_data.csv')

# Streamlit application settings
st.title('영화 추천 시스템')
st.write('영화를 선택하세요.')

# User selects a movie
selected_movie = st.selectbox('영화 선택', movie_df['title'].unique())

fav_genre = movie_df[movie_df['title'] == selected_movie]['parsed_genres']
#movie_df = movie_df[movie_df['title'] != selected_movie]

for movie in movie_df:
    matching_movies.append(vie_df[movie_df['parsed_genres'] == fav_genre]['title'])

# Display the matching movies
st.subheader('일치하는 영화')
for movie in matching_movies:
    st.write('- 영화 제목:', movie)
