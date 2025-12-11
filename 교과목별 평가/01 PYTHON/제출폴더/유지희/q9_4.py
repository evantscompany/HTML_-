# 4. 결과 파일로 저장 (선택 과제) 
# 각 학생의 총점과 평균도 계산하시오. 
# 각 학생의 이름, 총점, 평균을 포함한 새로운 CSV 파일(result.csv)로 저장하시오.

stues= []

with open('files/scores.csv','r',encoding='utf-8') as file:
    is_header= True
    for line in file:
        if is_header:
            is_header= False
            continue
        r=line.strip().split(',')

        stu=[r[0],int(r[1]),int(r[2]),int(r[3])]
        stues.append(stu)

stu_data= {}

for stu in stues:
    name=stu[0]
    scores=stu[1:]
    total=sum(scores)
    avg=round(total/len(scores),1)
    stu_data[name]={
        '총점:':total,
        '평균:':avg,
    }

    
print()
print('=======4번 문제(미완) 출력=======\n')
print(stu_data)


# stu=[]
# stu_data= {}

# with open('files/scores.csv','r',encoding='utf-8') as file:

#     f=file.readlines()[1:]

#     for line in f:
#         r= line.strip().split(',')
#         stu.append(r)

#     for a in stu:
#         name= a[0]
#         scores= list(map(int,a[1:]))        # 요소 하나하나를 형변환해서 넣어야 함
#         total= sum(scores)
#         avg= round(total/len(scores),1)     # round로 소수점 밑에 자리 조절
#         stu_data[name]={
#             '총점':total,
#             '평균':avg
#         }
# print(stu_data)