import streamlit as st
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Read the movie data
movie_df = pd.read_csv('test/movie_data.csv')

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Contents",
    ("Movie Recommendation", "Movie Lens", "Movie theater", "My page")
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
        
if add_selectbox == "Movie Lens":
    st.title("Movie Lens")
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

if add_selectbox == "Movie Lens":
    st.title("Movie recommendation system")
    st.subheader('Our top 5 movie picks ')
else:
   st.title("Movie recommendation system")
   st.subheader('Our top 5 movie picks ')     
