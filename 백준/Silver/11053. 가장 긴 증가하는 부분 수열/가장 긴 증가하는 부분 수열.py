import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

"""
dp 풀이법

dp = [1] * n

res = []
for i in range(n):
    for j in range(n - (n - i)):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)


print("dp : ",max(dp))
"""

"""
이진탐색
"""
def ezin(x,ez):

    start = 0
    end = len(ez)-1
    mid = ((start + end) // 2) 
    while start < end:
        mid = ((start + end) // 2) 

        if ez[mid] >= x: #중간값보다 작다면
            end = mid
        elif ez[mid] < x: #중간값보다 크다면
            start = mid+1 #나머지를 버렸으므로, 스타트값이 반복될수 있다.


    ez[end] = x

ez = [arr[0]]
for i in range(1,n):
    if ez[-1] < arr[i]:
        ez.append(arr[i])
    else:
        ezin(arr[i],ez)

print(len(ez))



