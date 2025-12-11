

with open('files/scores.csv', mode='r', encoding='UTF-8') as file:

    data = file.read()
    
    # 데이터 정리 - 이름, 성적
    data_list = [n for n in data.split('\n')]

    data_title = data_list[0].split(',')
    data_list = data_list[1:]
    
    # 각 과목 평균, 최고, 최저 점수
    subject_result = []
    for i in range(1, len(data_title)):

        total = 0
        max = 0
        min = 100

        for v in data_list:
            num = int(v.split(',')[i])

            if num > max: # 최대값
                max = num
            
            elif num < min: # 최소값
                min = num

            total = total + num # 총합

        # subject_result - 평균, 최대, 최소값 저장
        subject_result.append([total, max, min])

    for i in range(len(subject_result)):
        averge = subject_result[i][0] / len(data_list)
        max = subject_result[i][1]
        min = subject_result[i][2]

        print("{} - 평균: {:.1f}, 최고점 {}, 최저점: {}".format(data_title[i + 1], averge, max, min))

    print("-" * 50)

    for val in data_list:
        # 이름 , 성적
        li = val.split(',')

        total = sum([int(s) for s in li if s.isdigit()])
        averge = total / (len(li) - 1)

        print("{} - 총점 : {}, 평균 : {:.1f}".format(li[0], total, averge))

#data = pd.read_csv('files/scores.csv')






