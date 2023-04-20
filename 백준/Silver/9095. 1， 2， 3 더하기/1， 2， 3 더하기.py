import sys
input = sys.stdin.readline

M = int(input())
N = [int(input()) for _ in range(M)]

N_clon = sorted(N,reverse = True)
maxv = N_clon[0]

talList = [0] * (maxv+1)

for i in range(maxv+1):
    if i == 1:
        talList[1] = 1
    elif i == 2:
        talList[2] = 2
    elif i == 3:
        talList[3] = 4
    else:
        talList[i] = talList[i-1] + talList[i-2] + talList[i-3]

for i in N:
    print(talList[i])