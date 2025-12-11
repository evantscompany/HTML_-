student = {}

with open('./files/scores.csv', 'r', encoding='utf=8') as file :
    cnt = 0
    korean_list = []
    english_list = []
    math_list = []
    for line in file :
        if cnt == 0 :
            cnt += 1
            continue
        name, korean, english, math = line.split(',')
        korean, english, math = map(int,(korean, english, math))
        print('이름 :', name)
        print('국어 :', korean)
        print('영어 :', english)
        print('수학 :', math)   
        korean_list.append(korean)
        english_list.append(english)
        math_list.append(math)
        print()

        student[name] = [korean, english, math] #gpt 참고


    # 평균점수 산출
    korean_average = sum(korean_list) / len(korean_list)
    english_average = sum(english_list) / len(english_list)        
    math_average = sum(math_list) / len(math_list)    
    print('국어 평균:', korean_average)
    print('영어 평균:', english_average)
    print('수학 평균:', math_average)
    print()
    #최고점수 산출
    print('국어 최고점:', max(korean_list))
    print('영어 최고점:', max(english_list))
    print('수학 최고점:', max(math_list))
    print()
    #최저점수 산출
    print('국어 최저점:', min(korean_list))
    print('영어 최저점:', min(english_list))
    print('수학 최저점:', min(math_list))
    print()


    #결과 출력
    print(f"국어 - 평균: {korean_average}, 최고점: {max(korean_list)}, 최저점: {min(korean_list)}")
    print(f"영어 - 평균: {english_average}, 최고점: {max(english_list)}, 최저점: {min(english_list)}")
    print(f"수학 - 평균: {math_average}, 최고점: {max(math_list)}, 최저점: {min(math_list)}")
    print()
    
    # 학생별 총점과 평균 산출, gpt 참고
    for name, scores in student.items():
        total = sum(scores)
        aver = total / len(scores)
        print(f'{name}, 총점: {total}, 평균: {aver}')

import csv # csv로 저장
with open('result.csv', 'w', encoding='utf-8', newline='') as result_f :
    writer = csv.writer(result_f)

    writer.writerow(['이름', '총점', '평균'])
    
    for name, scores in student.items():
        total = sum(scores)
        aver = round(total / len(scores), 1)
        writer.writerow([name, total, aver])


    



   






