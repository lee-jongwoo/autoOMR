# ocr.py | 담당자: 이종우
# 이미지의 배열을 입력받아 ocr을 실행하고, 결과를 반환하는 함수.
# 숫자만 인식한다.

import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

def load():
    """
    학습된 모델을 한 번만 불러오는 함수
    :param model_path: 학습된 모델 파일 경로 (.h5)
    :return: 모델 객체
    """
    return load_model('models/mnist_model.h5')

def predict(model, img):
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
    pad = 10

    for contour in contours:
        # 윤곽선을 감싸는 사각형 영역 추출
        x, y, w, h = cv2.boundingRect(contour)
        if h > 10 and w > 10:  # 너무 작은 윤곽선은 무시
            start_x = np.clip(x - pad, 0, img.shape[1])
            start_y = np.clip(y - pad, 0, img.shape[0])
            end_x = np.clip(x + w + pad, 0, img.shape[1])
            end_y = np.clip(y + h + pad, 0, img.shape[0])
            digit = thresh[start_y:end_y, start_x:end_x]  # 숫자 영역 자르기

            # 28x28 크기로 조정 (MNIST 형식)
            resized_digit = cv2.resize(digit, (28, 28))

            # 모델 입력 형식에 맞게 정규화
            resized_digit = resized_digit.astype('float32') / 255
            resized_digit = np.expand_dims(resized_digit, axis=0)
            digits.append(resized_digit)

    # 예측 수행
    predictions = []
    for digit in digits:
        prediction = model.predict(digit)
        predicted_digit = np.argmax(prediction)
        predictions.append(predicted_digit)

    return sorted(predictions, key=lambda x: x)

# 테스트 코드
if __name__ == "__main__":
    model = load()
    image = cv2.imread("source/dummy/example_cropped.jpg", cv2.IMREAD_GRAYSCALE)
    predicted_digits = predict(model, image)
    print(predicted_digits)