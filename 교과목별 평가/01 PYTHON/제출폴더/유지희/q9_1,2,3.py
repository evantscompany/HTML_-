# 문제. 학생들의 성적이 저장된 scores.csv 파일을 이용한 성적 통계 프로그램을 만들어보시오. 

name= []
guk= []
young= []
su= []

# 1.
# CSV 파일 읽기 : open() 함수를 사용하여 scores.csv 파일을 읽으시오. 
# [* 첫줄(헤더)을 제외한 나머지 줄의 점수를 숫자(int) 데이터로 변환해야만 계산가능]

with open('files/scores.csv','r',encoding='utf-8') as file:
    is_header= True
    for line in file:
        if is_header:
            is_header= False
            continue
        row= line.strip().split(',')
        name.append(row[0])
        guk.append(int(row[1]))
        young.append(int(row[2]))
        su.append(int(row[3]))

# 2.
# 데이터 처리 : 각 과목(국어, 영어, 수학)에 대해 다음을 계산하시오. 
# 평균 점수 
# 최고 점수 
# 최저 점수 
print()
print('===========2번 문제 출력==========\n')
print(f''' ---국어 과목--
국 평균점:{sum(guk)/len(guk):.2f}
국 최저점:{min(guk)}
국 최고점:{max(guk)}''')
print()

print(f''' ---영어 과목--
영 평균점:{sum(young)/len(young):.2f}
영 최저점:{min(young)}
영 최고점:{max(young)}''')
print()

print(f''' ---수학 과목--
수 평균점:{sum(su)/len(su):.2f}
수 최저점:{min(su)}
수 최고점:{max(su)}''')
print()


# 3.
# 3. 결과 출력 : 각 과목별 통계 결과를 콘솔에 보기 좋게 출력하시오. 
# 예) 
# [과목별 통계] 
# 국어 - 평균: 85.5, 최고점: 92, 최저점: 76 
# 영어 - 평균: 88.0, 최고점: 94, 최저점: 80 
# 수학 - 평균: 84.0, 최고점: 95, 최저점: 72

print()
print('===========3번 문제 출력==========\n')

print('[과목별 통계]')
print(f'국어- 평균: {sum(guk)/len(guk):.1f}, 최고점: {max(guk)}, 최저점: {min(guk)}')
print(f'영어- 평균: {sum(young)/len(young):.1f}, 최고점: {max(young)}, 최저점: {min(young)}')
print(f'수학- 평균: {sum(su)/len(su):.1f}, 최고점: {max(su)}, 최저점: {min(su)}')



