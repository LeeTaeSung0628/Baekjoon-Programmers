def solution(Mlist, plays):
    dt_M = {i:Mlist[i] for i in range(len(Mlist))}
    dt_M = sorted(dt_M.items(),key = lambda x : x[1])
    
    j_dict = {} #장르별 최종 합
    jmax = [] #장르별 고유번호와 횟수
    total = 0 #장르별 합계
    maxv = 0 #장르별 최고값
    chek = "" #이전 장르값 저장
    
    # item[0] = 정렬될 비용, item = 정렬된 장르
    for item in dt_M:
        if chek == item[1]: #이전과 동일한 값이면
            total = total+plays[item[0]] #토탈에 값추가
            j_dict[chek] = total
        else:
            chek = item[1]  #새로운 장르가 도착하면 초기화 후 새장르값 추가
            total = plays[item[0]]
            j_dict[chek] = total
            
        jnn = [item[1],item[0],plays[item[0]]]
        jmax.append(jnn)
        
        chek = item[1]#현재 장르 저장
    
    
    j_dict = sorted(j_dict.items(),key = lambda x : -x[1])
    jmax = sorted(jmax, key = lambda x: (x[0],-x[2]))
    print(j_dict) #어느 장르를 먼저 뽑을건지
    print(jmax)
    
    answer = []
    chek2 = 0
    for item in j_dict:
        for i in range(len(jmax)):
            if jmax[i][0] == item[0] and chek2 < 2:
                answer.append(jmax[i][1])
                chek2 +=1
        chek2 = 0
 
    return answer