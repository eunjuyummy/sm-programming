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

movie_df = movie_df[movie_df['title'] != selected_movie]

matching_movies = movie_df[movie_df['parsed_genres'] == selected_movie]['title']

# Display the matching movies
st.subheader('일치하는 영화')
for movie in matching_movies:
    st.write('- 영화 제목:', movie)
