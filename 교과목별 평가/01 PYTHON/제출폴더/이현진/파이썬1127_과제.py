with open('files/scores.csv', 'r', encoding='utf-8') as file:
    contents = file.readlines()
    contents.pop(0)

    lang_tot = int()
    engl_tot = int()
    math_tot = int()
    

    lang_list = list()
    engl_list = list()
    math_list = list()

    for i in contents:
        info = i.strip().split(',')
        name = info[0]
        lang = int(info[1])
        engl = int(info[2])
        math = int(info[3])

        print(name)
        print('평균점수:', (lang+engl+math)/3)
        print('최고 점수:', lang if lang>engl and lang>math else engl if engl>math else math)
        print('최저 점수:', lang if lang<engl and lang<math else engl if engl<math else math)
        print('-'*30)

        
        lang_list.append(lang)
        engl_list.append(engl)
        math_list.append(math)


        lang_tot += lang
        engl_tot += engl
        math_tot += math

    print('[과목별 통계]')
    print(f'국어 - 평균: {lang_tot/len(contents)}, 최고점: {max(lang_list)}, 최저점: {min(lang_list)}')
    print(f'영어 - 평균: {engl_tot/len(contents)}, 최고점: {max(engl_list)}, 최저점: {min(engl_list)}')
    print(f'수학 - 평균: {math_tot/len(contents)}, 최고점: {max(math_list)}, 최저점: {min(math_list)}')




    