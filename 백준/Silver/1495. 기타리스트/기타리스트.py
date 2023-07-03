"""


"""
import sys
input = sys.stdin.readline

n, s, m = map(int,input().split())
arr = list(map(int,input().split()))

dp = [[False] * (m+1) for _ in range(n+1)]

#초기값 처리
dp[0][s] = True

for i in range(n): # +- 요소마다
    for j in range(m+1): #각 볼륨 값들 (0 ~ m)
        if dp[i][j] == True: #가능한 경우의 수 일때,
            if j + arr[i] <= m:
                dp[i+1][j+arr[i]] = True
            if j - arr[i] >= 0:
                dp[i+1][j-arr[i]] = True
            
checkLast = False
for d in range(m+1): #최대값이 True 인것중 가장 큰값
    if dp[-1][m-d] == True:
        print(m-d)
        checkLast = True
        break
if checkLast == False:
    print(-1)

