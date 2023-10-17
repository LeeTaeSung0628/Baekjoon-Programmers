def solution(x, y, n):
    answer = 0
    
    # 있는지 체크하면서 1씩 증가하는 방법
    dp = [[0,999999] for _ in range(y+1)]
    dp[x][0] = x
    dp[x][1] = 0
    
    for i in range(len(dp)):
        #나누어 떨어질때
        if i%2 == 0:
            #곱하기 전 값이 있다면
            if dp[int(i/2)][0] != 0:
                dp[i][0] = dp[int(i/2)][0] * 2
                dp[i][1] = min(dp[i][1] , dp[int(i/2)][1] + 1)
        
        if i%3 == 0:
            if dp[int(i/3)][0] != 0:
                dp[i][0] = dp[int(i/3)][0] * 3
                dp[i][1] = min(dp[i][1] , dp[int(i/3)][1] + 1)
    
        if i-n > 0:
            if dp[i-n][0] != 0:
                dp[i][0] = dp[i-n][0] + n
                dp[i][1] = min(dp[i][1] , dp[i-n][1] + 1)
                
    if dp[y][1] == 999999:
        return -1
    else:
        return dp[y][1]