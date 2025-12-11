#문제. 학생들의 성적이 저장된 scores.csv 파일을 이용한 성적 통계 프로그램을 만들어보시오.
#과제 요구사항
#1. CSV 파일 읽기 : open() 함수를 사용하여 scores.csv 파일을 읽으시오.
#[* 첫줄(헤더)을 제외한 나머지 줄의 점수를 숫자(int) 데이터로 변환해야만 계산가능]

name_list = []
kor_scores = []
eng_scores = []
math_scores = []

result_data = []

with open("files/scores.csv", "r", encoding='UTF-8') as file:

    next(file)

    for line in file:            #자동으로 readline하면서 반복수행함
        data_list=line.split(',')

        name = data_list[0]
        kor  = int(data_list[1])
        eng  = int(data_list[2])
        math = int(data_list[3])


#     print('이름:',data_list[0])
#     print('국어:',data_list[1])
#     print('영어:',data_list[2])
#     print('수학:',data_list[3])


        name_list.append(name)   # name_list 학생 이름의 순서대로 저장하는 리스트
        kor_scores.append(kor)   #국어점수
        eng_scores.append(eng)   #영어점수
        math_scores.append(math) #수학점수

        # 평균
        
        student_sum = (kor + eng + math)
        student_avg = (student_sum) / 3






