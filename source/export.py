# export.py | 담당자: 한지헌
# 처리된 성적 결과를 입력받아 csv 파일로 저장하는 함수.


def export(results, scores):
    # 여기부터 코드 작성
    data = []
    # results와 scores를 순회하며 형식 변환
    for student_id, answers in results.items():
        score = scores.get(student_id, 0)  # 학번에 해당하는 점수 가져오기, 기본값 0
        # 학번, 답변들, 점수를 포함한 리스트를 data에 추가
        data.append([int(student_id)] + answers + [score])

    # CSV 파일 저장
    with open("files/grades.csv", "w") as file:
        # 첫 줄에 헤더 작성
        file.write("학번, 답1, 답2, 답3, 답4, 답5, 점수\n")
        for row in data:
            # 각 row를 ','로 구분하여 파일에 작성
            file.write(",".join(map(str, row)) + "\n")


# 테스트를 위한 가짜 데이터
if __name__ == "__main__":
    results = {
        "10616": ["1", "2", "3", "4", "5"],
        "10617": ["1", "2", "3", "4", "5"],
        "10618": ["1", "2", "3", "4", "5"],
    }
    scores = {"10616": 4, "10617": 2, "10618": 3}
    export(results, scores)
