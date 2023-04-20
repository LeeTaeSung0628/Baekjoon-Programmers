import sys
input = sys.stdin.readline

X = int(input())

dp = [1] * (X+1) #찾을 수 만큼 배열을 지정
dp[0],dp[1] = 0,0 #0,1 일때는 연산횟수가 0 회이다.

for i in range(4,X+1): # 2,3은 1회로 고정이다. 
    # // 각 배열의 칸에는 몇번 연산해서 '1'이 될수 있는지 저장되어있다.
    if i % 2 == 0 and i % 3 == 0: #두개 다 가능할때
        dp[i] = min(dp[int(i/3)],dp[int(i/2)],dp[i-1]) +1
    elif i % 3 == 0: # 3으로 나누어 떨어지면
        dp[i] = min(dp[int(i/3)],dp[i-1]) +1 # +1은 연산횟수 1회 추가다.
    elif i % 2 == 0: # 2로 나누어 떨어지면
        dp[i] = min(dp[int(i/2)],dp[i-1]) +1
    else:
        dp[i] = dp[i-1] +1


#print(dp)

print(dp[X])