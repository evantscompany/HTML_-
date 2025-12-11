# 문제2.
# 사용자로부터 정수 2개를 입력받아서 둘 중 작은 값을 구하여 출력하는 프로그램을 작성하시오. 
# 단, 같은 값이면 그 값이 출력되도록 하시오.

num1= int( input('num1 : ') )
num2= int( input('num2 : ') )

if num1<num2:
    print('작은 값 :', num1)
else:
    print('작은 값 :', num2)