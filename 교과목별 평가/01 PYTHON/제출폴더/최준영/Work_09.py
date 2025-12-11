subject_scores={'국어':[],'영어':[],'수학':[]}
with open('Files/scores.csv','r',encoding='utf-8') as file:
    contents=file.readline()
    for line in file:
        이름,국어,영어,수학=line.strip().split(',')
        subject_scores['국어'].append(int(국어))
        subject_scores['영어'].append(int(영어))
        subject_scores['수학'].append(int(수학))
for subject, scores in subject_scores.items():
    avg = sum(scores) / len(scores)
    maximum = max(scores)
    minimum = min(scores)
        
    print(f'--- [{subject} 점수 통계] ---')
    print(f'{subject} 점수의 평균: {avg:.1f}')
    print(f'{subject} 점수 중 최고점은 {maximum}점 입니다.')
    print(f'{subject} 점수 중 최저점은 {minimum}점 입니다.')
    print()
print('== 과목별 통계 ==')
print(f'국어 -- 평균 : {sum(subject_scores['국어'])/len(subject_scores['국어']):.1f}  최고점 : {max(subject_scores['국어'])}  최저점 : {min(subject_scores["국어"])}')
print(f'영어 -- 평균 : {sum(subject_scores['영어'])/len(subject_scores['영어']):.1f}  최고점 : {max(subject_scores['영어'])}  최저점 : {min(subject_scores["영어"])}')
print(f'수학 -- 평균 : {sum(subject_scores['수학'])/len(subject_scores['수학']):.1f}  최고점 : {max(subject_scores['수학'])}  최저점 : {min(subject_scores["수학"])}')



























# print(f'국어 점수의 평균: {(sum(subject_scores['국어']))/len(subject_scores['국어']):.1f}')
# print(f'국어 점수중 최고점은 {max(subject_scores['국어'])}점 입니다.')
# print(f'국어 점수중 최저점은 {min(subject_scores['국어'])}점 입니다.')
# print()
# print(f'영어 점수의 평균: {(sum(subject_scores['영어']))/len(subject_scores['영어']):.1f}')
# print(f'영어 점수중 최고점은 {max(subject_scores['영어'])}점 입니다.')
# print(f'영어 점수중 최저점은 {min(subject_scores['영어'])}점 입니다.')
# print()
# print(f'수학 점수의 평균: {(sum(subject_scores['수학']))/len(subject_scores['수학']):.1f}')
# print(f'수학 점수중 최고점은 {max(subject_scores['수학'])}점 입니다.')
# print(f'수학 점수중 최저점은 {min(subject_scores['수학'])}점 입니다.')
