# preprocessing.py | 담당자: 신우협
# 이미지 하나를 입력받아 openCV를 이용해 직사각형 모서리를 감지, 답란을 추출하여 배열로 반환하는 함수.

import cv2
import numpy as np

# 입력: image
# 출력: image (cv2)의 array


def preprocess(image):
    min_area = 1000
    padding = 5

    # 이미지 그레이스케일 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지 블러 처리
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 윤곽선 찾기
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 좌표를 담을 배열
    boxes = []

    for cnt in contours:
        # 직사각형 감싸기
        x, y, w, h = cv2.boundingRect(cnt)

        # 최소 면적 필터링
        if w * h < min_area:
            continue

        # 패딩 적용하여 사각형 좌표 조정
        x_padded = x + padding
        y_padded = y + padding
        w_padded = w - 2 * padding
        h_padded = h - 2 * padding

        # 테두리 윤곽선이 제거된 답란 좌표 추가
        boxes.append((y_padded, x_padded, w_padded, h_padded))

    # y좌표를 기준으로 정렬
    boxes = sorted(boxes, key=lambda b: b[0])

    return [image[y : y + h, x : x + w] for y, x, w, h in boxes]


# 테스트를 위한 가짜 데이터.
if __name__ == "__main__":
    image = cv2.imread("source/dummy/example.jpg")
    for image in preprocess(image):
        cv2.imshow("image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
