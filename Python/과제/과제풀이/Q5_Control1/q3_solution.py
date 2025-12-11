# 문제3.
# 사용자로부터 정수 3개를 입력받아 정수형 변수 a, b, c 에 각각 저장한 후, 
# 조건문을 사용하여 이들 변수 중 가장 큰 값을 가진 변수의 값을 max라는 이름의 정수형 변수에 대입하고 출력하는 프로그램을 작성하시오.

a= int(input('input: '))
b= int(input('input: '))
c= int(input('input: '))

#방법1)
if a>b and a>c:
    max= a
elif b>c:
    max= b
else:
    max= c

print("가장 큰 값은 :", max)

# --------------------------

#방법2)
max= a
if( max<b ): max= b
if( max<c ): max= c 
print("가장 큰 값은 :", max)



