import streamlit as st
import pandas as pd
import pandas as pd
import folium
import matplotlib.pyplot as plt
from PIL import Image

# Read the movie data
movie_df = pd.read_csv('test/movie_data.csv')

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Contents",
    ("Movie Recommendation", "Data analytics", "Movie theater", "Setting")
)

if add_selectbox == "Movie Recommendation":
    # Streamlit application settings
    st.title("Movie recommendation system")
    #image = Image.open('sunrise.jpg')

    #st.image(image, caption='Sunrise by the mountains')

    # User selects a movie
    selected_movie = st.selectbox("movie list", movie_df['title'].unique())

    # Get the genre of the selected movie
    selected_genre = movie_df.loc[movie_df['title'] == selected_movie, 'parsed_genres'].values[0]

    # Filter movies with the same genre and sort by rating
    matching_movies = movie_df.loc[movie_df['parsed_genres'] == selected_genre]
    sorted_movies = matching_movies.sort_values('rating', ascending=False).head(5)

    st.subheader('Your favorite movie genre is ' + selected_genre)
    # Display the top 5 movies with the highest rating from the same genre
    st.subheader('Our top 5 movie picks ')

    for index, row in sorted_movies.iterrows():
        st.write('title', row['title'])
        
elif add_selectbox == "Data analytics":
    st.title("Data analytics")
    st.subheader('Count the number of movies per genre')
    # Count the number of movies per genre
    genre_counts = movie_df['parsed_genres'].value_counts()

    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(genre_counts.index, genre_counts.values)

    # Customize the chart
    ax.set_xlabel('genres')
    ax.set_ylabel('count')
    ax.set_xticklabels(genre_counts.index, rotation=90)

    # Display the chart in Streamlit
    st.pyplot(fig)
    
    st.subheader('TOP 5 highest rated movies')
    sorted_movies = movie_df.sort_values('rating', ascending=False).head(5)
    
    num = 1
    for index, row in sorted_movies.iterrows():
        st.write('Top', num)
        st.write(' 영화 제목:', row['title'])
        st.write('  평점:', row['rating'])
        st.write('  장르:', row['parsed_genres'])
        st.write('--------------------------------')
        num += 1

    
elif add_selectbox == "Movie theater":
    st.title("Movie recommendation system")
    st.subheader('Our top 5 movie picks ')

    # Streamlit application settings
    st.title('지도 시각화')

    # Create a map object using Folium
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=13)

    # Add markers to the map
    folium.Marker([37.5665, 126.9780], popup='서울 시청').add_to(m)
    folium.Marker([37.5649, 126.9982], popup='광화문').add_to(m)

    # Display the map in Streamlit
    folium_static(m)

    
else:
   # Streamlit application settings
    st.title('Add a new movie')
    st.subheader('Movie List')
    st.write(movie_df)
    
    # Prompt the user for movie details
    new_title = st.text_input('title')
    genres = movie_df['parsed_genres'].unique()
    new_genre = st.selectbox('genres', genres)
    new_rating = st.slider('How old are you?', 0.0, 5.0, 0.5)
    # Add the new movie to the DataFrame
    new_movie = {'title': new_title, 'parsed_genres': new_genre, 'rating': new_rating}
    st.subheader('New Movie')
    st.write('Title: ', new_title, 'Genres: ', new_genre, 'Rating: ', new_rating)
