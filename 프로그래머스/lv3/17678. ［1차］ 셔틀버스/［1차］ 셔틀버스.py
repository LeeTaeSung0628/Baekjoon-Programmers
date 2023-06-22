def solution(n, t, m, table):
    
    #인원별 도착시간 분으로 바꾸기
    mtable = []
    for item in table:
        hour = int(item[0]+item[1])
        minut = int(item[3]+item[4])
        mtable.append((hour*60)+minut)
    
    # 9시 정각은 540이다.
    mtable = sorted(mtable,key = lambda x : -x)
    #대기줄 배열
    q = []
    
    roll = 0 #버스가 몇번 왔는지
    while roll < n: #다음버스가 없을때까지
        
        #버스 도착시간
        busTime = 540+ (roll*t)
        roll += 1 #버스 도착 ( 처음 버스는 540분에 도착 )
        
        #버스 도착시간보다 일찍도착한사람 최대 m명만 태우고 출발~
        maxP = 0
        tempP = [] #임시 승객배열
        while maxP < m:
            if len(mtable) > 0 and mtable[-1] <= busTime:
                maxP+=1
                tempP.append(mtable.pop())
            else: break

        if roll == n: #마지막버스면
            #만약 대시 승객이 있을때
            if len(tempP) > 0:
                #자리가 꽉찼을때
                if len(tempP) == m:#마지막 애보다 1분 일찍오면 돼
                    ansTime = tempP[m-1]-1
                    h = str(ansTime // 60)
                    h = h.zfill(2)
                    m = str(ansTime % 60)
                    m = m.zfill(2)
                    return h+":"+m
                else:#자리가 남으면 버스시간에 맞춰서 오면 돼
                    h = str(busTime // 60)
                    h = h.zfill(2)
                    m = str(busTime % 60)
                    m = m.zfill(2)
                    return h+":"+m
            else:
                h = str(busTime // 60)
                h = h.zfill(2)
                m = str(busTime % 60)
                m = m.zfill(2)
                return h+":"+m
        
        
    answer = ''
    return answer