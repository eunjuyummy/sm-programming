import streamlit as st
import pandas as pd

# Read the movie data
movie_df = pd.read_csv('test/movie_data.csv')

# Streamlit application settings
st.title('영화 추천 시스템')
st.write('영화를 선택하세요.')

# 이미지 버튼 클릭 시 실행될 함수
def button_clicked():
    st.write('이미지 버튼이 클릭되었습니다!')

# 이미지 버튼 생성
button_image = st.image('test/image/As Above.jfif', caption='이미지 버튼')

# 이미지 버튼을 클릭하면 실행될 함수를 버튼에 연결
if button_image.button('클릭'):
    button_clicked()
