import streamlit as st
import pandas as pd
from PIL import Image

# Read the movie data
movie_df = pd.read_csv('test/movie_data.csv')

# Streamlit application settings
st.title('영화 추천 시스템')
st.write('영화를 선택하세요.')


#image = Image.open('sunrise.jpg')

#st.image(image, caption='Sunrise by the mountains')

# User selects a movie
selected_movie = st.selectbox('영화 선택', movie_df['title'].unique())

# Get the genre of the selected movie
selected_genre = movie_df.loc[movie_df['title'] == selected_movie, 'parsed_genres'].values[0]

# Filter movies with the same genre and sort by rating
matching_movies = movie_df.loc[movie_df['parsed_genres'] == selected_genre]
sorted_movies = matching_movies.sort_values('rating', ascending=False).head(5)

# Display the top 5 movies with the highest rating from the same genre
st.subheader('Top 5 영화')
for index, row in sorted_movies.iterrows():
    st.write('- 영화 제목:', row['title'])
    st.write('  평점:', row['rating'])
    st.write('  장르:', row['parsed_genres'])
