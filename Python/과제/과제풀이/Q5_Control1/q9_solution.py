# 문제9. 
# 사용자로부터 정수 3개를 입력받아 아래를 수행하세요.

# 1. 세 수 중 가장 큰 값 출력
# 2. 세 수의 평균 계산
# 3. 평균이 70 이상이면 "통과", 아니면 "불합격" 출력
# 4. 평균이 정수인지 실수인지 판단하여 "정수 평균" 또는 "실수 평균" 출력
# (힌트: float은 소문자가 있어요.  )    <-- 오타가 있네요. 소수점이 있어요.. 입니다. ㅜㅜ
# (힌트: float은 소수점 아래가 있어요. 즉. 나눗셈의 나머지값이 있어요.  )

num1 = int(input('input number : '))
num2 = int(input('input number : '))
num3 = int(input('input number : '))

#1.
m= num1
if m<num2: m=num2
if m<num3: m=num3
print('세 수 중 가장 큰 값 :', m)

#2.
total= num1+num2+num3
average= total/3
print('세 수의 평균 :', average)

#3.
if average>=70:
    print('통과')
else:
    print('불합격')

#4. 
if total%3==0:   # 평균이 과목수 3으로 나눈것이므로 3으로 나누어 떨어지면(나머지가 0이면) 정수. 그렇지 않으면 소수점 아래 존재하니 실수
    print('정수 평균')
else:
    print('실수 출력')

# ---------------------------------------------
print('~'*40)


# 배우진 않았으나(나중에 함수 수업시간에 일부 소개예정) 파이썬에 내장된 기능함수를 이용하여 쉽게 문제 1, 4 번 해결하기

#1. max() 함수
print('세 수 중 가장 큰 값 :', max(num1, num2, num3)) 
# [주의! 위에서 max라는 변수를 만들어 사용했다면. 내장함수 max()가 인식되지 않음.]

#4. 실수형 숫자의 기능함수 .is_integer() <-- 소수점 아래가 0인지 여부..
if average.is_integer():
    print('정수 평균')
else:
    print('실수 출력')

