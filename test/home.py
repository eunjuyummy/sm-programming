import streamlit as st
import pandas as pd

# Read the movie data
movie_df = pd.read_csv('test/movie_data.csv')

# Streamlit application settings
st.title('영화 추천 시스템')
st.write('영화를 선택하세요.')

# User selects three movies
selected_movies = st.multiselect('영화 선택', [str(title) for title in movie_df['title'].unique()], [], 3)

if len(selected_movies) == 3:
    # Initialize lists to store matching movies
    matching_movies = []

    # Find favorite genres for selected movies
    fav_genres = movie_df[movie_df['title'].isin(selected_movies)]['parsed_genres'].tolist()

    # Filter movies by favorite genres and remove selected movies from the DataFrame
    filtered_df = movie_df[movie_df['parsed_genres'].isin(fav_genres) & ~movie_df['title'].isin(selected_movies)]

    # Group movies by title and calculate the average rating
    grouped_df = filtered_df.groupby('title').agg({'rating': 'mean'}).reset_index()

    # Sort movies by rating in descending order
    sorted_df = grouped_df.sort_values('rating', ascending=False)

    # Display the top 3 movies for each favorite genre
    st.subheader('일치하는 영화')

    for genre in fav_genres:
        # Get the top 3 movies for the current genre
        top_movies = sorted_df[sorted_df['parsed_genres'] == genre].head(3)

        if not top_movies.empty:
            st.subheader('장르: {}'.format(genre))
            for index, row in top_movies.iterrows():
                st.write('- 영화 제목: {} (평점: {:.2f})'.format(row['title'], row['rating']))
        else:
            st.write('장르 {}에 대한 일치하는 영화가 없습니다.'.format(genre))
else:
    st.write('3개의 영화를 선택해야 합니다.')
