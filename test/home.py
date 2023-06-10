import streamlit as st
import pandas as pd
from PIL import Image

# Read the movie data
movie_df = pd.read_csv('test/movie_data.csv')

# Streamlit application settings
st.title('영화 추천 시스템')
st.write('영화를 선택하세요.')

# 이미지 버튼 클릭 시 실행될 함수
def button_clicked():
    st.write('Image button clicked!')

# Load the image
image = Image.open('test/image/apollo13.jpg')

# Display the image and button
col_image, col_button = st.beta_columns([1, 1])
with col_image:
    st.image(image, use_column_width=True)

with col_button:
    if st.button('Click me!', help='Image button', on_click=button_clicked):
        pass


#image = Image.open('sunrise.jpg')

#st.image(image, caption='Sunrise by the mountains')


