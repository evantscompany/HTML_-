#문제1.
#사용자로 부터 정수 하나를 입력받아라. 입력받은 정수의 절대값을 출력하는 프로그램을 작성하시오.

num= int(input('input number : '))

if num<0:
    print('|num|:', -num)
else:
    print('|num|:', num)
