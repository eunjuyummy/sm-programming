import streamlit as st
import pandas as pd

# 영화 데이터를 읽어온다
movies_df = pd.read_csv('test/movie_data.csv')

# Streamlit 애플리케이션 설정
st.title('영화 추천 시스템')
st.write('영화를 선택하세요.')

# 사용자에게 영화 선택을 받는다
selected_movie = st.selectbox('영화 선택', movies_df['title'].unique())

# 선택한 영화의 장르를 확인한다
selected_genre = movies_df[movies_df['title'] == selected_movie]['parsed_genres'].values[0]

# 같은 장르의 영화 중 평점이 높은 상위 3개를 추천한다
recommended_movies = movies_df[(movies_df['parsed_genres'] == selected_genre).nlargest(3, 'rating')

# 추천 영화를 출력한다
st.subheader('추천 영화')
for index, row in recommended_movies.iterrows():
    st.write('- 제목:', row['title'], '| 평점:', row['rating'])
