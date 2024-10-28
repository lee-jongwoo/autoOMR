# preprocessing.py | 담당자: 신우협
# 이미지 하나를 입력받아 openCV를 이용해 직사각형 모서리를 감지, 답란을 추출하여 배열로 반환하는 함수.

import cv2
import numpy as np

def preprocess(image):
  # 입력: image
  # 출력: image (cv2)의 array

  # 여기부터 코드 작성
  images = np.array()

  return images

# 테스트를 위한 가짜 데이터.
image = cv2.imread('example.jpg')
print(preprocess(image))