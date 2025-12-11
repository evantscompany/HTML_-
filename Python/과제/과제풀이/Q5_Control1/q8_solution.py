# 문제8. 문자열 안 특정 단어 포함 여부 확인
# 사용자로부터 문장을 입력받아,
# 해당 문장에 "error" 라는 단어가 포함되어 있으면 "오류 포함" 
# 없으면 "정상"이라고 출력하세요.
# (대소문자 구분 없이 처리)

sentence= input('Please enter a sentence in English. : ')

if 'error' in sentence.lower():
    print('오류 포함')
else:
    print('정상')