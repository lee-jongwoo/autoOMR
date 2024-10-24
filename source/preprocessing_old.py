# 10/24에 작성한 코드 백업.
# 이후 수정된 코드는 preprocessing.py에 작성됨.

import cv2

# 이미지 불러오기
image = cv2.imread('example.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

# 윤곽선 찾기
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 윤곽선 순회
for contour in contours:
    # 사각형 모양인지 확인 (윤곽선 근사화)
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    # 사각형일 경우
    if len(approx) == 4:
        # 사각형 외곽선을 이미지에 그리기
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)

# 결과 보여주기
cv2.imshow('Detected Squares', image)
cv2.waitKey(0)
cv2.destroyAllWindows()