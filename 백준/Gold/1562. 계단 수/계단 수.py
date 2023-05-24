import sys
input = sys.stdin.readline

n = int(input())

#dp[자리수][끝자리값][상태(0~9)]
dp = [[[0]*1024 for _ in range(10)] for _ in range(n+1)]

#초기화
for i in range(1,10): # 0000000001 , 00001000000, 1000000000 등으로 채움
    dp[1][i][0 | ( 1 << i)] = 1

for i in range(1,n):#모든계단에 대해서
    for j in range(10):#끝자리값 상태
        for k in range(1024): #모든 체크상태에 대해서
            if j < 9:
                dp[i+1][j+1][k | (1 << j+1)] += dp[i][j][k]
            if j > 0:
                dp[i+1][j-1][k | (1 << j-1)] += dp[i][j][k]

res = 0
for i in range(10):
    res += dp[n][i][1023]
            
print(res % 1000000000)
