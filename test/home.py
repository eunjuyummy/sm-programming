import streamlit as st
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.header('All About Movies :movie_camera:')
st.title('Movie Lens')
st.markdown("<hr>", unsafe_allow_html=True)

# Read the movie data
movie_df = pd.read_csv('test/movie_data.csv')

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Contents",
    ("Movie Recommendation", "Data analytics", "Setting")
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

    st.subheader('Your favorite movie :blue[genre] is ' + selected_genre)
    
    # 선택한 장르에 따라 어울리는 이미지 출력
    if selected_genre == 'Adventure':
        image = Image.open('test/image/toystory.jpg')
        st.image(image, caption="This isn't Flying This is falling with style", width=300)
    elif selected_genre == 'Animation':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Children':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Comedy':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Fantasy':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Romance':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Drama':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Action':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Crime':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Thriller':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Horror':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Mystery':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Sci-Fi':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'War':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Musical':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'Documentary':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    elif selected_genre == 'IMAX':
        st.Image('test/image/toystory.jpg', caption='Image Caption')
    else:
        st.Image('test/image/toystory.jpg', caption='Image Caption')
   
        
        
       
    
    
    
    # Display the top 5 movies with the highest rating from the same genre
    st.subheader('Our top 5 movie picks ')
    for index, row in sorted_movies.iterrows():
        st.subheader('Title')
        st.write(row['title'])
        
        
        
        
elif add_selectbox == "Data analytics":
    st.title("Data analytics")
    
    tab1, tab2 = st.tabs(["Count", "Top5"])

    with tab1:
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
        
        
    with tab2:
        st.header('TOP 5 highest rated movies')
        sorted_movies = movie_df.sort_values('rating', ascending=False).head(5)

        num = 1
        for index, row in sorted_movies.iterrows():
            st.subheader('Top', num)
            st.subheader(' 영화 제목:', row['title'])
            st.subheader('  평점:', row['rating'])
            st.subheader('  장르:', row['parsed_genres'])
            st.subheader('--------------------------------')
            num += 1

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
    
    
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.caption('_This is :blue[the Movie Lens] where you can find all about the movie._ :sunglasses:')
