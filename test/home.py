# import 라이브러리
import streamlit as st
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def on_button_click():
    # movie data csv 파일 읽어오는 코드
    movie_df = pd.read_csv('test/movie_data.csv')

    # 사이드바 구현하는 코드 
    add_selectbox = st.sidebar.selectbox(
        "Contents",
        ("Movie Recommendation", "Data analytics", "Setting")
    )

    # Movie Recommendation 페이지 
    if add_selectbox == "Movie Recommendation":
        st.title("Movie recommendation system")

        # movie list에서 영화를 선택하는 select box
        selected_movie = st.selectbox("movie list", movie_df['title'].unique())

        # 선택한 영화의 장르를 가져온다
        selected_genre = movie_df.loc[movie_df['title'] == selected_movie, 'parsed_genres'].values[0]

        # 같은 장르의 영화를 필터링하고 평점이 높은 순으로 나열해 top5개의 영화만 가져온다
        matching_movies = movie_df.loc[movie_df['parsed_genres'] == selected_genre]
        sorted_movies = matching_movies.sort_values('rating', ascending=False).head(5)

        # User가 선택한 장르를 알려준다.
        st.subheader('Your favorite movie :blue[genre] is ' + selected_genre)

        # 선택한 장르에 따라 어울리는 이미지 출력
        if selected_genre == 'Adventure':
            image = Image.open('test/image/toystory.jpg')
            st.image(image, caption="This isn't Flying This is falling with style", width=300)
        elif selected_genre == 'Animation':
            image = Image.open('test/image/bighero.jpg')
            st.image(image, caption="I'm not giving up on you.", width=300)
        elif selected_genre == 'Children':
            image = Image.open('test/image/matilda.jpg')
            st.image(image, caption="matilda.", width=300)
        elif selected_genre == 'Comedy':
            image = Image.open('test/image/dlu.jpg')
            st.image(image, caption="Washington's always gotta have a hero", width=300)
        elif selected_genre == 'Fantasy':
            image = Image.open('test/image/herry.jpg')
            st.image(image, caption="It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.", width=300)
        elif selected_genre == 'Romance':
            image = Image.open('test/image/titanic.jpg')
            st.image(image, caption="I know, only you can do that", width=300)
        elif selected_genre == 'Drama':
            image = Image.open('test/image/martian.jpg')
            st.image(image, caption="I don't wanna come off as arrogant here, but I'm best botanist on the planet.", width=300)
        elif selected_genre == 'Action':
            image = Image.open('test/image/john.jpg')
            st.image(image, caption="Such is life.", width=300)
        elif selected_genre == 'Crime':
            image = Image.open('test/image/crime.jpg')
            st.image(image, caption="To the truth room.", width=300)
        elif selected_genre == 'Thriller':
            image = Image.open('test/image/us.jpg')
            st.image(image, caption="us", width=300)
        elif selected_genre == 'Horror':
            image = Image.open('test/image/us.jpg')
            st.image(image, caption="us", width=300)
        elif selected_genre == 'Mystery':
            image = Image.open('test/image/mys.jpg')
            st.image(image, caption="mystery", width=300)
        elif selected_genre == 'Sci-Fi':
            image = Image.open('test/image/avarta.jpg')
            st.image(image, caption="All energy is only borrowed and one day you have to give it back", width=300)
        elif selected_genre == 'War':
            image = Image.open('test/image/in.jpg')
            st.image(image, caption="The abandonment of ideals wrinkles the soul.", width=300)
        elif selected_genre == 'Musical':
            image = Image.open('test/image/lala.jpg')
            st.image(image, caption="Just go with the flow", width=300)
        elif selected_genre == 'Documentary':
            image = Image.open('test/image/mar.jpg')
            st.image(image, caption="March of the Penguins", width=300)
        elif selected_genre == 'IMAX':
            image = Image.open('test/image/avarta.jpg')
            st.image(image, caption="All energy is only borrowed and one day you have to give it back", width=300)
        else:
            image = Image.open('test/image/noir.jpg')
            st.image(image, caption="film noir history.", width=300)

        # 동일한 장르에서 평점이 가장 높은 상위 5개의 영화를 보여준다
        st.subheader('상위 5개의 추천 영화')
        st.subheader('Our top 5 movie picks ')
        num = 1                                  
        for index, row in sorted_movies.iterrows():
            st.write(num ,row['title'])
            num += 1


    # Data analytics 페이지                
    elif add_selectbox == "Data analytics":
        st.title("Data analytics")

        #  탭 생성
        tab1, tab2 = st.tabs(["Count", "Top5"])

        # tab1
        with tab1:
            st.subheader('Count the number of movies per genre')
            # 장르별 영화 수 세기
            genre_counts = movie_df['parsed_genres'].value_counts()

            # 막대 그래프 그리기
            fig, ax = plt.subplots()
            ax.bar(genre_counts.index, genre_counts.values)
            ax.set_xlabel('genres')
            ax.set_ylabel('count')
            ax.set_xticklabels(genre_counts.index, rotation=90)
            st.pyplot(fig)

        # tab2  
        with tab2:
            st.subheader('TOP 5 highest rated movies')
            # 평점이 높은 순으로 데이터를 정렬하고 가장 높은 5개의 영화를 선택 
            sorted_movies = movie_df.sort_values('rating', ascending=False).head(5)

            # 데이터프레임의 각 행의 인덱스와 해당 행을 가져와 5개의 영화를 순서대로 보여주는 코드 
            num = 1
            for index, row in sorted_movies.iterrows():
                st.write('Top', num)
                st.write(' Title:', row['title'])
                st.write(' Rating:', row['rating'])
                st.write('  Genres:', row['parsed_genres'])
                st.write('--------------------------------')
                num += 1


    # setting 페이지           
    else:
        st.title('Add a new movie')
        st.subheader('Movie List')
        # 데이터 프레임을 보여준다
        st.write(movie_df)

        # User로 부터 새로운 정보를 입력 받는 코드 
        new_title = st.text_input('title')

        # 이미 존재하는 영화의 경우 이미 존재한다는 message 출력
        if new_title in movie_df['title'].values:
           st.subheader('The movie already exists.')
        else:
            genres = movie_df['parsed_genres'].unique() 
            new_genre = st.selectbox('genres', genres)
            new_rating = st.slider('How satisfied were you with the movie?', 0.0, 5.0, 0.5)

            # 데이터 프레임에 추가할 영화에 대한 정보를 보여준다
            new_movie = {'title': new_title, 'parsed_genres': new_genre, 'rating': new_rating}  # 구현X
            st.subheader('New Movie')
            st.write('Title: ', new_title, '     Genres: ', new_genre, '     Rating: ', new_rating)


# 하단 페이지    
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.caption('_This is :blue[the Movie Lens] where you can find all about the movie._ :sunglasses:')
    
    
# 메인 베너를 구현하는 코드 
st.header('All About Movies :movie_camera:')     
st.title('Movie Lens')                          
st.markdown("<hr>", unsafe_allow_html=True)

if st.button("클릭하세요"):
    on_button_click()


