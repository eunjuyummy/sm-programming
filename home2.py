import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def bmi_range(bmi):
    if bmi >= 25:
        st.error("비만 입니다")
        image = Image.open('koala.jpg')
        st.image(image, caption='cute koala')
    elif bmi >= 23:
        st.warning("과체중 입니다")
        image = Image.open('koala.jpg')
        st.image(image, caption='cute koala')
    elif bmi >= 18.5:
        st.success("정상 입니다.")
        image = Image.open('koala.jpg')
        st.image(image, caption='cute koala')
    else:
        st.warning("저체중 입니다")    
        image = Image.open('koala.jpg')
        st.image(image, caption='혹시 당신 초식동물?')   
        
# 체질량 지수 구하는 
# 몸무게, 키 입력 받기

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "목차",
    ("체질량 계산기", "Gap minder", "my page")
)

if add_selectbox == "체질량 계산기":
    
    st.write("# 체질량 계산기")
    st.info('체질량지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.', icon="ℹ️")

    height = st.number_input('키를 입력하세요. (cm)',100,200,170,5)
    st.write('키:', height,'cm')

    weight = st.number_input('체중 (kg)',value = 50, step = 5)
    st.write('키:', height,'cm')

    bmi = weight/(height/100)**2

    if st.button('계산'):
        st.write('당신의 체질량 지수는', round(bmi,2),'입니다.')
        bmi_range(bmi)
        
    st.balloons()
    
elif add_selectbox == "Gap minder":
    st.write("# 여기는 Gap minder입니다.")

    data = pd.read_csv('gapminder.csv')
    
    st.write(data)
    
    colors=[]
    
    for x in data['continent']:
        if x == 'Asia':
            colors.append('tomato')
        elif x == 'Europe':
            colors.append('blue')
        elif x == 'Africa':
            colors.append('olive')
        elif x == 'Americas':
            colors.append('green')
        else:
            colors.append('orange')
            
    year = st.slider('연도를 선택하세요.', 1952, 2007, 1952, step = 5)
    st.write("year: ", year, '입니다.')

    data = data[data['year']==year]
    
    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'], data['lifeExp'], s=data['pop']*0.000002, color=data['colors'])
    ax.set_title("How Does Gap per Capital relate to Life Expectancy?")
    ax.set_xlabel("Gap per Capital")
    ax.set_ylabel('Life Expectancy')
    
    st.pyplot(fig)
  

else:
    st.write("# 여기는 my page입니다.")
    



    
