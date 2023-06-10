import streamlit as st
import pandas as pd

# 영화 데이터를 읽어온다
movies_df = pd.read_csv('movie_table.csv')

# Streamlit 애플리케이션 설정
st.title('영화 추천 시스템')
st.write('영화를 선택하세요.')

# 사용자에게 영화 선택을 받는다
selected_movie = st.selectbox('영화 선택', movies_df['영화 제목'].unique())

# 선택한 영화의 장르를 확인한다
selected_genre = movies_df[movies_df['영화 제목'] == selected_movie]['장르'].values[0]

# 같은 장르의 영화 중 평점이 높은 상위 3개를 추천한다
recommended_movies = movies_df[(movies_df['장르'] == selected_genre) & (movies_df['평점'] > 8)].nlargest(3, '평점')

# 추천 영화를 출력한다
st.subheader('추천 영화')
for index, row in recommended_movies.iterrows():
    st.write('- 제목:', row['영화 제목'], '| 평점:', row['평점'])
