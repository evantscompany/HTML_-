# 문제2.
# 섭씨(Celsius)온도를 입력하면 화씨(Fahrenheit)온도를 반환하는 cel_to_fah라는 이름의
# 함수와 그 반대로 화씨 온도를 입력하면 섭씨 온도를 반환하는 fah_to_cel라는 이름의
# 함수를 정의하고 이 두 함수를 호출하는 예제를 완성해 보자. 참고로 섭씨와 화씨간의
# 온동변환의 공식은 다음과 같다.

#    Fah=1.8*Cel+32


def cel_to_fah(cel):
    return 1.8*cel+32

def fah_to_cel(fah):
    return (fah-32)/1.8


c= float(input('섭씨 온도 : '))
f= cel_to_fah(c)
print('화씨 온도 :', f)

print()

f= float(input('화씨 온도 : '))
c= fah_to_cel(f)
print('썹씨 온도 :', c)