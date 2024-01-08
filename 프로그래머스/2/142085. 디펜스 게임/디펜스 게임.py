import heapq

def solution(n, k, enemy):
    
    """
     병사 n명
     공격을 순서대로 막는다.
     내 병사 수 만큼 적을 막을 수 있다.
     적이 더 많으면 게임 종료
     * 무적권을 사용하면 k번 병력소모 없이 한라운드 공격을 막을 수 있다.
     
     하나씩 더해주면서, 최대값을 스텍에 넣는다. 
     더했을때, n의 범위를 넘어가면 k를 하나 줄이고, n의 값을 증가시켜준다.
     
    """
    
    q = []
    maxv = 0
    
    for i in range(len(enemy)):
        # print("전 : ",n)
        n -= enemy[i]
        
        #현재 만난 적군사 수를 우선순위 큐에 삽입
        heapq.heappush(q,enemy[i]*-1)
        
        if n < 0:
            if k > 0: # 무적권 사용
                # 저장 후 사용
                temp = heapq.heappop(q) * -1
                # print("temp : ", temp)
                n += temp
                
                k -= 1
            else:
                return i #이전 라운드 까지만 막은것
        # print("후 : ",n)
    
    return len(enemy)