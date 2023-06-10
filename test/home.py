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
button_clicked = st.button(label='클릭', key='image_button', help='이미지 버튼', on_click=button_clicked, 
                           type='default', key_button=0, key_scope='image_button_scope',
                           help_button='이미지 버튼 도움말', args_button={}, kwargs_button={},
                           tooltip=None, disabled_button=False, auto_on_click=True,
                           draggable=True, key_draggable=None)

# 이미지 버튼에 이미지 추가
button_clicked.image('test/image/apollo13.jpg', width=200, caption='이미지 버튼')
