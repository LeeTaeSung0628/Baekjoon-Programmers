
import sys

input = sys.stdin.readline

S1 = input().strip()
S2 = input().strip()

#재귀적 호출로 지정
def LCS(x, y):
    m, n = len(x), len(y)
    #둘 중 하나라도 다 사라지면
    if m == 0 or n == 0:
        return 0
    else:
        if x[-1] == y[-1]: #맨 끝글자가 동일하다면
            return LCS(x[:m-1] , y[:n-1]) + 1 #한칸씩 줄이고 값1 증가
        else:
            return max( LCS(x[:m-1] , y), LCS(x , y[:n-1]) )

#dp 테이블 만들기
def LCS_DP(x,y):
    x, y  = " " + x , " " + y
    m, n = len(x), len(y)
    #각 문자열의 길이+1 만큼 dp테이블 생성(첫칸은 0으로 채우기)
    dp = [[0] * n for _ in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            #문자열이 똑같다면
            if x[i] == y[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]

    
print(LCS_DP(S1, S2))

"""
CBDA
ACADB
"""