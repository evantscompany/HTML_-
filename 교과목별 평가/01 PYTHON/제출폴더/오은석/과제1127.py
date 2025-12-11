def pars_cvs(r_data) :
    return list(map(lambda x:int(x.strip()) if str(x.strip()).isdecimal() else x.strip() , r_data.split(",")))

rdata = []
rslt1 = ["[과목별 통계]"]
rslt2 = ["[개인별 통계]"]

with open("C:\\Users\\Admin\\MBCA\\scores.csv", "r", encoding="UTF-8") as fread:
    scr_date = fread.readlines()
    titl = pars_cvs(scr_date[0])
    # print(titl)
    for scr in scr_date[1:] :
        l_data = pars_cvs(scr)
        rdata.append(l_data)
        # print(l_data)
        rslt2.append(f"이름 : {l_data[0]} , 총점 : {sum(l_data[1:]):3d} , 평균 : {sum(l_data[1:])/(len(l_data)-1):2.1f}")
    
    # print(rdata)
    for i in range(len(titl)-1) :
        rslt1.append(f"{titl[i+1]} - 평균 : {sum(list(map(lambda x:x[i+1] , rdata)))/len(rdata):.1f}" +
                     f" , 최고점 : {max(list(map(lambda x:x[i+1] , rdata)))}" +
                     f" , 최저점 : {min(list(map(lambda x:x[i+1] , rdata)))}")

with open("C:\\Users\\Admin\\MBCA\\scores_prc.csv", "w", encoding="UTF-8") as fread:
    for i in rslt1 :
        fread.write(i+"\n")
        print(i)
    for i in rslt2 :
        fread.write(i+"\n")
        print(i)