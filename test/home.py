import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model

# 학습된 모델 로드
model = load_model('your_model.h5')  # 학습된 모델 파일로 대체해야 함

# 카메라로부터 이미지 캡처 함수
def capture_image():
    cap = cv2.VideoCapture(0)
    _, frame = cap.read()
    cap.release()
    return frame

# 이미지 전처리 함수
def preprocess_image(image):
    # 이미지를 흑백으로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 이미지 크기 조정 및 정규화
    resized = cv2.resize(gray, (28, 28))
    normalized = resized / 255.0
    # 차원 추가 (모델 입력 형태로 변환)
    processed = np.expand_dims(normalized, axis=0)
    return processed

# 손글씨 숫자 예측 함수
def predict_digit(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    predicted_label = np.argmax(prediction)
    confidence = np.max(prediction) * 100
    return predicted_label, confidence

# 앱 제목과 설명
st.title('손글씨 숫자 맞추기')
st.write('카메라로부터 캡처한 손글씨 이미지를 이용하여 숫자를 맞춥니다.')

# 카메라로부터 이미지 캡처
captured_image = capture_image()

# 캡처한 이미지 표시
st.image(captured_image, channels='BGR', caption='캡처한 이미지')

# 숫자 예측
predicted_digit, confidence = predict_digit(captured_image)

# 예측 결과 및 신뢰도 표시
st.write(f'예측된 숫자: {predicted_digit}')
st.write(f'신뢰도: {confidence:.2f}%')
