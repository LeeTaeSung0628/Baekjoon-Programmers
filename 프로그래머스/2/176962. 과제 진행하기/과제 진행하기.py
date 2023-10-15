def solution(plans):
    
    #플랜의 시작시간을 분의 int 형태로 변환한다.
    for i in range(len(plans)):
        _, p2, p3 = plans[i]
        plans[i][1] = (int(p2[:2])*60) + int(p2[3:])
        plans[i][2] = int(p3)
    
    #정렬 후 새로 담기
    pl = sorted(plans, key = lambda x:x[1])
    
    
    """
    1. 제일빠른녀석의 시간을 기준으로 걸리는 시간사이에 과제가 있는지 체크
     1.1 걸리는시간을 더한 시간 사이에 진행할 과제가 있다면, (그과제의 시작시간 - 진행중인 과제의 시작시간) 만큼 진행중인과제의 남은시간을 저장한다
         1로 돌아간다.
     1.2 사이에 진행할 과제가 없다면, 잠시멈춰둔과제중 가장 최근에 멈춰둔 녀석부터 시작한다.
         1로 돌아간다.
    2. 더이상 진행할 과제가 없다면, 멈춰둔과제를 최근순으로 모두 마친다.
    """
    answer = []
    
    #잠시멈춰둔 과제와, 남은시간을 저장
    stop = []
    
    for i in range(len(pl)):
        
        #마지막과제라면
        if i == len(pl)-1:
            answer.append(pl[i][0])
            continue
        
        #현재 과제를 마칠수 있는가?
        if pl[i][1]+pl[i][2] == pl[i+1][1]:
            answer.append(pl[i][0])
        #마치고도 시간이 남는다면
        elif pl[i][1]+pl[i][2] < pl[i+1][1]:    
            answer.append(pl[i][0])
            #멈춰둔 과제가 있다면
            if stop:
                #남은시간만큼 최대한 과제를 수행한다.
                leftTime = pl[i+1][1] - (pl[i][1]+pl[i][2])
                while stop:
                    item = stop.pop()
                    #수행해야될 시간보다 남은시간이 길면 수행하기
                    if item[1] <= leftTime:
                        answer.append(item[0])
                        leftTime -= item[1]
                    #수행할 수 없다면
                    else:
                        item[1] -= leftTime
                        stop.append(item)
                        break
                    
        else:
            #남은시간과 함께 저장
            temp = []
            temp.append(pl[i][0])
            temp.append( pl[i][2] - (pl[i+1][1] - pl[i][1]) )
            stop.append(temp)
    
    #멈춰둔 과제 전부 수행
    while stop:
        item = stop.pop()
        answer.append(item[0])
    
    return answer