# 문제1.
# 세 개의 정수를 인자로 전달받아서 그 중 가장 큰 수를 반환하는 함수와 가장 작은 수를
# 반환하는 함수를 정의해 보자. 그리고 이 함수를 호출하는 프로그램도 작성해보자.
# [파이썬 내장함수 min, max를 직접 만들어 보아요. 함수의 이름은 각자 적절한 식별자를 명명하시오.]

def get_max(a,b,c):
    max=a
    if max<b: max=b
    if max<c: max=c

    return max

def get_min(a,b,c):
    min=a
    if min>b: min=b
    if min>c: min=c

    return min

max_value= get_max(10,50,30)
print('max value :', max_value)

min_value= get_min(10,50,30)
print('min value :', min_value)