import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp = [1] * n

res = []
for i in range(n):
    for j in range(n - (n - i)):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)


print(max(dp))

