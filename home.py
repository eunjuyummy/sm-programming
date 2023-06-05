import streamlit as st

# 체질량 지수 구하는 
# 몸무게, 키 입력 받기

height = st.number_input('키를 입력하세요. (cm)',100,200,170,5)
st.write('키:', height,'cm')