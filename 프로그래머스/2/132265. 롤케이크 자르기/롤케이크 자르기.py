def solution(topp):
    """
    한번 쫙 스캔하면서
    좌를 기준으로 토핑개수
    우를 기준으로 토핑개수를 매핑한다.
    ex) 1 2 2 3 3 4 4 4
        4 4 4 4 3 3 2 1 

    겹치는 부분 쳌
    """
    
    left = []
    ldic = {}
    right = []
    rdic = {}
    
    #좌측맵핑
    now = 0
    for i in range(len(topp)):
        #새로운 토핑이면
        if topp[i] not in ldic:
            ldic[topp[i]] = 1
            now += 1
        
        left.append(now)
        

    
    #우측맵핑
    now = 0
    for i in range(len(topp)):
        n = len(topp) - i-1
        #새로운 토핑이면
        if topp[n] not in rdic:
            rdic[topp[n]] = 1
            now += 1
        
        right.append(now)
    
    right.reverse()

    answer = 0
    
    #갯수 새기
    for i in range(len(topp)-1):
        #left는 0부터 n-1까지
        #right는 1부터 n까지
        if left[i] == right[i+1]:
            answer += 1
    
    
    return answer