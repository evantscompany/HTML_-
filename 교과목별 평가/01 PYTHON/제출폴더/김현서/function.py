lang_scores = []
eng_scores = []
math_scores = []
students=[]

with open('files/scores.csv','r',encoding='utf-8') as file:
    lines= file.readlines()
    for line in lines[1:]:
        name,lang,eng,math=line.strip().split(',')
        if lang.isdigit and eng.isdigit and math.isdigit:
            lang=int(lang)
            eng = int(eng)
            math=int(math)

            lang_scores.append(lang)
            eng_scores.append(eng)
            math_scores.append(math)

            total = lang + eng + math
            avg =total/3
            students.append([name,total,avg])
    
#국어 
    print('국어 평균:',sum(lang_scores)/len(lang_scores))
    print('국어 최고 점수:', max(lang_scores))
    print('국어 최저 점수:', min(lang_scores))
    print()

#영어
    print('영어 평균:', sum(eng_scores)/len(eng_scores))
    print('영어 최고 점수:',max(eng_scores))
    print('영어 최저 점수:',min(eng_scores))
    print()

#수학
    print('수학 평균:',sum(math_scores)/len(math_scores))
    print('수학 최고 점수:', max(math_scores))
    print('수학 최저 점수:', min(math_scores))
    print()
print('과목별 통계')


lang_average= sum(lang_scores)/len(lang_scores)
lang_max= max(lang_scores)
lang_min= min(lang_scores)

eng_average= sum(eng_scores)/len(eng_scores)
eng_max= max(eng_scores)
eng_min= min(eng_scores)

math_average = sum(math_scores)/len(math_scores)
math_max = max(math_scores)
math_min = min(math_scores)

print(f'국어 - 평균 : {lang_average}, 최고점 : {lang_max}, 최저점 : {lang_min}')
print(f'영어 - 평균 : {eng_average}, 최고점 : {eng_max}, 최저점 : {eng_min}')
print(f'수학 - 평균 : {math_average}, 최고점 : {math_max}, 최저점 : {math_min}')

print()
print('각 학생의 총점과 평균')
print(students)

with open('result.csv','w',encoding='utf-8') as file:
    file.write('이름,총점,평균\n')
    for stu in students:
        name, total,avg = stu
        file.write(f'{name},{total},{avg}\n')

print('result.csv 저장 완료!')