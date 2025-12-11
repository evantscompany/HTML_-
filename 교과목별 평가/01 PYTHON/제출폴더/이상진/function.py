
# 함수 function 과제 #2

name_list = []
kor_scores = []
eng_scores = []
math_scores = []

result_data = []

with open("C:/Users/Admin/MBCA/Python/Pyinstaller/scores.csv", "r", encoding='UTF-8') as file:


    next(file)


#   보통의 표형태의 데이터 구조는 한줄에 한 아이템의 정보들이 존재함.
#   그래서 한줄 단위로 읽어서 처리...
    
    for line in file: # 자동으로 readline()을 하면서 반복수행함.

        data_list = line.strip().split(',') # CSV 파일에서는 한줄에 여러 데이터가 콤마(,)로 나뉘어져 있음. 
                                            # split(',')하게 되면 리스트 요소로 변환됨
        
        name = data_list[0]
        kor  = int(data_list[1])
        eng  = int(data_list[2])
        math = int(data_list[3])

        # print('이름 : ', name)
        # print('국어 : ', kor)
        # print('영어 : ', eng)
        # print('수학 : ', math)
    
        name_list.append(name)   # name_list 학생 이름의 순서대로 저장하는 리스트
        kor_scores.append(kor)
        eng_scores.append(eng)
        math_scores.append(math)

        # 학생별 평균 계산
        
        student_sum = (kor + eng + math)
        student_avg = student_sum / 3

        # result_data에 저장 (이름, 국어, 영어, 수학, 총점, 평균)
        result_data.append([name, kor, eng, math, student_sum, student_avg])

kor_average = sum(kor_scores)/len(kor_scores)
eng_average = sum(eng_scores)/len(eng_scores)
math_average = sum(math_scores)/len(math_scores)

kor_max = max(kor_scores)
eng_max = max(eng_scores)
math_max = max(math_scores)

kor_min = min(kor_scores)
eng_min = min(eng_scores)
math_min = min(math_scores)

# 각 과목별 총 8명의 점수를 과목 List에 저장

print('학급 명단 : ', name_list)
print('국어 점수 : ', kor_scores)
print('영어 점수 : ', eng_scores)
print('수학 점수 : ', math_scores)

# 과목 별 최고, 최저 점수

print('국어 최고 {} / 최소 {}'.format(kor_max, kor_min))
print('영어 최고 {} / 최소 {}'.format(eng_max, eng_min))
print('수학 최고 {} / 최소 {}'.format(math_max, math_min))

# 각 과목별 평균 점수

print('국어 평균 : ', kor_average)
print('영어 평균 : ', eng_average)
print('수학 평균 : ', math_average)


# result_data = (name_list) + (kor_scores) + (eng_scores) + (math_scores)

# with open("scores_copy.csv", "w", encoding="UTF-8") as dst:
#    dst.write(data_list)    # 새로운 이름으로 저장

# with open("result.csv", "w", encoding="UTF-8") as rst:
#    rst.write(str(result_data))    # 새로운 이름으로 저장


with open("result.csv", "w", encoding="UTF-8") as rst:
    rst.write("이름,국어,영어,수학,총점,평균\n")
    for row in result_data:
        rst.write(",".join([str(v) for v in row]) + "\n")

print("result.csv 파일 저장 완료!")
