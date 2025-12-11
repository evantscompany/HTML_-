# 문제12.
# 사용자로부터 하나의 문장을 입력받아 다음 기준에 따라 문장의 “유형”을 판단하세요.

# 규칙:
# - 감탄사 "!" 로 끝나면 → "감탄 문장"
# - 물음표 "?" 로 끝나면 → "의문 문장"
# - 문장 길이가 30자 이상이면 → "긴 문장"
# - 문장에 숫자가 하나라도 포함되어 있으면 → "숫자 포함 문장"

# 위 조건 중 해당되는 모든 유형을 출력하세요.

# 예)
# 입력: "Python is amazing! 123"
# 출력: "감탄 문장, 긴 문장, 숫자 포함 문장"

# [ hint: 문자열 끝 글자 확인, in, .isdigit() ]
# [ hint: 문자열 끝 글자 확인, in, .replace() – 비효율적인 반복 작업이 필요합니다. ]

sentence= input("문장을 입력하세요: ")

result = ""

# 1. 
if sentence.endswith("!"):
    if result: result += ", "
    result += "감탄 문장"    

# 2. 
if sentence.endswith("?"):
    if result: result += ", "
    result += "의문 문장"

# 3.
if len(sentence) >= 30:
    if result: result += ", "
    result += "긴 문장"    

# 4. 숫자 모양 문자가 있는지 확인 (반복문을 사용하지 않기에 코드가 다소 비효율적임)
#방법1)
has_number= ('0' in sentence) or ('1' in sentence) or ('2' in sentence) or ('3' in sentence) or ('4' in sentence) or ('5' in sentence) or ('6' in sentence) or ('7' in sentence) or ('8' in sentence) or ('9' in sentence)
#방법2)
new_sentence= sentence.replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
has_number= new_sentence != sentence
if has_number:
    if result: result += ", "
    result += "숫자 포함 문장"
    

print(result)