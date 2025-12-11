# scores.csv 파일 읽기
filename = "scores.csv"

students = []
with open(filename, "r", encoding="utf-8") as f:
    header = f.readline().strip().split(",")   # ["이름", "국어", "영어", "수학"]
    
    for line in f:
        name, kor, eng, math = line.strip().split(",")
        students.append({
            "이름": name,
            "국어": int(kor), #숫자는 int로 변환
            "영어": int(eng),
            "수학": int(math)
        })

# 과목별 점수 리스트 만들기
kor_scores = [s["국어"] for s in students]
eng_scores = [s["영어"] for s in students]
math_scores = [s["수학"] for s in students]

# 과목별 통계 계산 함수
def stats(scores):
    return sum(scores) / len(scores), max(scores), min(scores)

kor_avg, kor_max, kor_min = stats(kor_scores)
eng_avg, eng_max, eng_min = stats(eng_scores)
math_avg, math_max, math_min = stats(math_scores)

# 결과 출력
print("[과목별 통계]")
print(f"국어 - 평균: {kor_avg:.1f}, 최고점: {kor_max}, 최저점: {kor_min}")
print(f"영어 - 평균: {eng_avg:.1f}, 최고점: {eng_max}, 최저점: {eng_min}")
print(f"수학 - 평균: {math_avg:.1f}, 최고점: {math_max}, 최저점: {math_min}")

# ===========================================
# 선택 과제: result.csv로 저장
# ===========================================
with open("result.csv", "w", encoding="utf-8") as f:
    f.write("이름,총점,평균\n")
    for s in students:
        total = s["국어"] + s["영어"] + s["수학"]
        avg = total / 3
        f.write(f"{s['이름']},{total},{avg:.1f}\n")

print("\nresult.csv 파일이 생성되었습니다.")
