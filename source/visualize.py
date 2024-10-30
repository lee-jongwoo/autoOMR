# visualize.py | 담당자: 오형진
# 성적 점수 자료를 입력받아 분포를 시각화하는 함수.

import matplotlib.pyplot as plt
import platform


def visualize(results, answerkey, scores):
    # 여기부터 코드 작성

    # 한글 폰트 설정
    os = platform.system()
    if os == "Windows":
        plt.rc("font", family="Malgun Gothic")
    elif os == "Darwin":
        plt.rc("font", family="AppleGothic")

    # 학번을 x축, 점수를 y축으로 하는 막대 그래프
    plt.figure()
    plt.bar(results.keys(), scores.values())
    plt.xlabel("학번")
    plt.ylabel("점수")
    plt.title("성적 분포")

    # 문항별 정답률을 계산하여 그래프로 표시
    correct = [0] * len(answerkey)
    total = [0] * len(answerkey)
    for student, recognized in results.items():
        for i, answer in enumerate(recognized):
            total[i] += 1
            if answer == answerkey[i]:
                correct[i] += 1
    correct_rate = [c / t for c, t in zip(correct, total)]

    plt.figure()
    plt.plot(range(1, len(answerkey) + 1), correct_rate, marker="o")
    plt.xticks(range(1, len(answerkey) + 1))
    plt.ylim(0, 1)
    plt.xlabel("문항 번호")
    plt.ylabel("정답률")
    plt.title("문항별 정답률")
    plt.show()


# 테스트를 위한 가짜 데이터
if __name__ == "__main__":
    results = {
        "10616": ["1", "2", "3", "4", "5"],
        "10617": ["1", "2", "3", "4", "5"],
        "10618": ["1", "2", "3", "4", "5"],
    }
    scores = {"10616": 4, "10617": 2, "10618": 3}
    answerkey = ["1", "2", "3", "4", "5"]
    visualize(results, answerkey, scores)
