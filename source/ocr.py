# ocr.py | 담당자: 이종우
# 이미지의 배열을 입력받아 ocr을 실행하고, 결과를 반환하는 함수.
# 숫자만 인식한다.

import cv2
import numpy as np
from tensorflow.keras import models

def load_ocr_model():
    """
    학습된 모델을 한 번만 불러오는 함수
    :param model_path: 학습된 모델 파일 경로 (.h5)
    :return: 모델 객체
    """
    return models.load_model("weights/mnist_cnn.weights.h5")

def predict_digits_from_image(model, img):
    """
    이미지에서 숫자를 추출하고 예측하는 함수
    :param model: 불러온 모델 객체
    :param img: 예측할 이미지 파일 (cv grayscale 이미지)
    :return: 예측된 숫자의 리스트
    """

    # 이미지 전처리: 이미지 읽기 및 이진화
    _, thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)

    # 윤곽선 찾기
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    digits = []

    for contour in contours:
        # 윤곽선을 감싸는 사각형 영역 추출
        x, y, w, h = cv2.boundingRect(contour)
        if h > 10 and w > 10:  # 너무 작은 윤곽선은 무시
            digit = thresh[y:y+h, x:x+w]  # 숫자 영역 자르기

            # 28x28 크기로 조정 (MNIST 형식)
            resized_digit = cv2.resize(digit, (28, 28))

            # 모델 입력 형식에 맞게 정규화
            resized_digit = resized_digit.astype('float32') / 255
            resized_digit = np.expand_dims(resized_digit, axis=-1)  # (28, 28, 1)
            digits.append(resized_digit)

    # 예측 수행
    predictions = []
    for digit in digits:
        digit = np.expand_dims(digit, axis=0)  # (1, 28, 28, 1)
        prediction = model.predict(digit)
        predicted_digit = np.argmax(prediction)
        predictions.append(predicted_digit)

    return sorted(predictions, key=lambda x: x)
