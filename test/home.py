import streamlit as st
import pandas as pd

# Assuming you have the recommended_movies DataFrame
# Read the movie data
movies_df = pd.read_csv('test/movie_data.csv')

# Streamlit application settings
st.title('영화 추천 시스템')
st.write('영화를 선택하세요.')

# User selects a movie
selected_movie = st.selectbox('영화 선택', movies_df['title'].unique())

# Filter the selected movie from the DataFrame
selected_movie_data = recommended_movies[movies_df['title'] == selected_movie]

# Display the selected movie's details
if not selected_movie_data.empty:
    st.subheader('선택한 영화')
    st.write(selected_movie_data)

# Display the recommended movies
st.subheader('추천 영화')
#for index, row in recommended_movies.iterrows():
#    st.write('- 제목:', row['영화 제목'], '| 평점:', row['평점'])
