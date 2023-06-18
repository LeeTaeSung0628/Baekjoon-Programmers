def solution(alp, cop, problems):
    
    #목표치(요구치) 구하기
    al = 0
    co = 0
    for item in problems:
        al = max(al,item[0])
        co = max(co,item[1])
    
    alp = min(al,alp)
    cop = min(co,cop)
    
    INF = float("inf")
    #dp 배열 생성
    dp = [[INF] * (co+1) for _ in range(al+1)] #가장큰 상승치만큼 더해준다
    dp[alp][cop] = 0 #기본값일때 소모시간은 0이다
    
    #모든 문제를 다 풀수 있을때 까지 반복(가장큰 요구치를 넘어설때까지)
    #목표치를 포함해서 돌린다.
    for a in range(alp,al+1):
        for c in range(cop,co+1):
            #코딩력 알고력 공부하는 경우의 수
            if a + 1 <= al:
                dp[a+1][c] = min(dp[a][c]+1,dp[a+1][c])
            if c + 1 <= co:
                dp[a][c+1] = min(dp[a][c]+1,dp[a][c+1])  
            
            #풀수있는 문제 푸는 경우의 수
            for p in problems:
                if a >= p[0] and c >= p[1]:
                    next_a = min(al, a+p[2])
                    next_c = min(co, c+p[3])
                    dp[next_a][next_c] = min(dp[a][c] + p[4], dp[a][c] + (p[2]+p[3]), dp[next_a][next_c])
                    
    print(dp)

    minans = dp[al][co]

    print(dp[al][co])
            
    if minans == INF:
        return 0
    else:
        return minans