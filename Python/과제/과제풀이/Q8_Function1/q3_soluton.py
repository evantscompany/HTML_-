# 문제3.
# 프로그램 사용자로부터 두개의 정수를 입력 받아서 구구단을 출력하는 프로그램을 작성해 보자. 
# 예를 들어서 프로그램 사용자가 3과 5를 입력하면 3단,4단,5단이 출력되어야 하고, 2와 6을 입력하면 2단,3단,4단,5단,6단이 출력되어야 한다.
# 단 한가지 조건이 있다. 사용자는 두개의 숫자를 입력 할 때에 입력 순서에 자유로워야한다. 즉, 3과5을 입력하건 5와 3을 입력하던 프로그램은 같은 결과를 출력해야 한다.

# - 개발 절차 -
# 두 개의 정수를 인자로 전달받아서 두 수 사이의 구구단을 출력하는 함수를 정의하고, 이 함수를 호출하는 형태로 구현해 보자.


def show_gugudan( start, end ):
    if start>end:
        start,end= end,start #서로가 가진 값을 교환... [파이썬언어만의 독특한 대입 문법]

    for dan in range(start, end+1):
        for i in range(1,10):
            print('{} x {} = {}'.format(dan, i, dan*i))
        print()

start_dan= int(input('시작 단 : '))
end_dan= int(input('종료 단 : '))
print()

show_gugudan(start_dan, end_dan)


