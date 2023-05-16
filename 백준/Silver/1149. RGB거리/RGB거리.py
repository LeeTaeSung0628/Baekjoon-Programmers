"""
    아이디어 : 1 ~ N번 까지 집
             빨강 초록 파랑 중 하나의 색으로 칠해야 한다.
             
             1번 2번 집은 색이 같이 않아야 한다.
             N번집의 색은 N-1번집의 색과 같지 않아야 한다.
            2 <= i <= N-1 일때  i는 (i-1번집,i+1번) 집과 색이 같지 않아야한다.
            
            N = 3 빨/파/빨 가능 

            dp로 각각을 선택했을때 얻을수 있는 최소값을 저장한다.
                각각의 값은 이전값과 같지 않아야한다. 이 점만 지킨다면 아무제약이 없다.

            26 / 40 / 83
            89 / 86 / 83
            96 / 100+ / 100+
"""
import sys

input = sys.stdin.readline

n = int(input())
rgb = [list(map(int,input().split())) for _ in range(n)]

INF = float("inf") #양의 무한대
dp = [[INF] * 3 for _ in range(n)]
dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]

for i in range(1,len(rgb)):
    for j in range(3): # 0~2
        if j == 0:
            dp[i][j] = rgb[i][j]+min(dp[i-1][1],dp[i-1][2])
        elif j == 1:
            dp[i][j] = rgb[i][j]+min(dp[i-1][0],dp[i-1][2])
        elif j == 2:
            dp[i][j] = rgb[i][j]+min(dp[i-1][0],dp[i-1][1])

print(min(dp[-1]))