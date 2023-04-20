import sys
input = sys.stdin.readline

N = int(input())

talList = [0] * (N+1) 

for i in range(N+1):
    if i == 1:
        talList[1] = 1
    elif i == 2:
        talList[2] = 2
    else:
        talList[i] = talList[i-1] + talList[i-2]

print(talList[N]%10007)