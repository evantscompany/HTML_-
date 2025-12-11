# 문제5.
# 문제 4번의 내용을 if~else를 사용하여 해결하였는가? 이를 if~else의 한줄쓰기 문법인 삼항연산자를 이용하여 구현해 보자. 
# (A if(조건) else B)

num1= int(input('input: '))
num2= int(input('input: '))

sub= num1- num2 if(num1>num2) else num2-num1
print("두 수의 차이: ", sub)