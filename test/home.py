import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model

# MNIST 데이터셋 로드
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 학습된 모델 로드
model = load_model('test/your_model.h5')  # 학습된 모델 파일로 대체해야 함

# 앱 제목과 설명
st.title('MNIST 손글씨 맞추기')
st.write('이 앱은 0부터 9까지의 손글씨 숫자를 맞추는 데 사용됩니다.')

# 손글씨 숫자 선택
selected_image = st.selectbox('손글씨 숫자를 선택하세요.', range(10))

# 선택한 숫자에 대한 이미지 표시
st.image(X_test[selected_image], width=150, caption=f'선택한 숫자: {y_test[selected_image]}')

# 선택한 숫자에 대한 예측 결과
prediction = model.predict(np.expand_dims(X_test[selected_image], axis=0))
predicted_label = np.argmax(prediction)
st.write(f'예측 결과: {predicted_label}')

# 모델의 신뢰도 점수
confidence = np.max(prediction) * 100
st.write(f'신뢰도: {confidence:.2f}%')
