# 문제10.
# 사용자로부터 파일명을 하나 입력받아 아래를 판단하세요.

# 예) report_2025_final.csv

# 1. 파일 이름에 "2025"가 들어 있으면 "올해 파일"
# 2. "report"로 시작하면 "보고서 유형"
# 3. ".csv"로 끝나면 "CSV 데이터 파일"

# 위 조건 중 해당되는 것들을 모두 출력 (해당되는 것이 여러 개일 수 있음)
# 출력 예) “올해 파일, 보고서 유형, CSV 데이터 파일”
# ( hint: .startswith(), .endswith(), in )
# (hint: .startswith(), .endswith(),in, 문자열 누적 결합연산으로 결과 만들어요.)

file_name = input("파일명을 입력하세요: ")

result = ""      # 출력될 문자열
is_first = True     # 앞에 콤마를 찍을지 여부 판단용

# 1. "2025" 포함 여부
if "2025" in file_name:
    if not is_first:
        result += ", "
    result += "올해 파일"
    is_first = False

# 2. "report"로 시작하는지
if file_name.startswith("report"):
    if not is_first:
        result += ", "
    result += "보고서 유형"
    is_first = False

# 3. ".csv"로 끝나는지
if file_name.endswith(".csv"):
    if not is_first:
        result += ", "
    result += "CSV 데이터 파일"
    is_first = False

print(result)

# ----------------------------------------

#방법2)
# is_first 변수를 사용하는 것이 지저분해 보인다면..
# result 가 빈글씨가 아니면 이전에 추가된 글씨가 있다는 것이니 ', '를 찍도록..

result = ""      # 출력될 문자열

# 1. "2025" 포함 여부
if "2025" in file_name:
    if result: result += ", "
    result += "올해 파일"

# 2. "report"로 시작하는지
if file_name.startswith("report"):
    if result: result += ", "
    result += "보고서 유형"

# 3. ".csv"로 끝나는지
if file_name.endswith(".csv"):
    if result: result += ", "
    result += "CSV 데이터 파일"

print(result)

# ----------------------------------------

#방법3)
# 금요일에 배울 '리스트'를 사용하면 더 쉬워짐.
results = []   # 조건에 맞는 문구를 저장할 리스트

# 1. "2025"가 들어 있으면
if "2025" in file_name:
    results.append("올해 파일")

# 2. "report"로 시작하면
if file_name.startswith("report"):
    results.append("보고서 유형")

# 3. ".csv"로 끝나면
if file_name.endswith(".csv"):
    results.append("CSV 데이터 파일")

# 결과 출력 (여러 개일 수 있음)
print(", ".join(results))