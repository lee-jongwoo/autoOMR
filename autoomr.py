import os
import numpy as np
from pdf2image import convert_from_path

from source.preprocessing import preprocess
from source.ocr import load, predict
from source.export import export
from source.visualize import visualize

os.chdir(os.path.dirname(__file__))

# 걍 이런거 너무 해보고 싶었음
print(
    """
              _         ___  __  __ ____  
   __ _ _   _| |_ ___  / _ \\|  \\/  |  _ \\ 
  / _` | | | | __/ _ \\| | | | |\\/| | |_) |
 | (_| | |_| | || (_) | |_| | |  | |  _ < 
  \\__,_|\\__,_|\\__\\___/ \\___/|_|  |_|_| \\_\\
   v1.0             (c) 2024, Team autoOMR
                                          """
)

print("Initializing...")

# PDF 파일과 정답표 불러오기
try:
    pages = convert_from_path("files/input.pdf")
    print("PDF file loaded.")
except:
    print("Error: PDF file not found.")
    print("Be sure to place input.pdf in the 'files' directory.")
    exit()
try:
    answerkey = open("files/answers.txt", "r").read().splitlines()
    print("Answer key loaded.")
except:
    print("Error: Answer key not found.")
    print("Be sure to place answers.txt in the 'files' directory.")
    exit()

# OCR 모델 불러오기
model = load()
results = {}
print("CNN Model loaded.")
input("Press Enter to start processing...")

# PDF 파일 페이지별로 이미지 추출 및 OCR
for i, page in enumerate(pages):
    image = np.array(page)
    croppedrects = preprocess(image)
    answers = []
    for img in croppedrects:
        text = predict(model, img)
        answers.append(text)
    if answers:
        results[answers[0]] = answers[1:]
    else:
        print(f"No answers found on page {i+1}. Skipping...")

# 학번 순으로 정렬
results = dict(sorted(results.items()))
print(results)

# 정답표와 비교하여 점수 계산
print("Recognition complete. Grading...")
scores = {}
for student, recognized in results.items():
    score = 0
    for i, answer in enumerate(recognized):
        if answer == answerkey[i]:
            score += 1
    scores[student] = score
print(scores)

# 성적 분포 시각화
print("Done. Displaying graph...")
visualize(results, answerkey, scores)

# 결과를 CSV 파일로 내보내기
print("Exporting results to CSV...")
export(results, scores)

print("All done. Check the 'files' directory for the results.")
