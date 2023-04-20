import sys

input = sys.stdin.readline

N = int(input()) #구입할 카드 개수
C = list(map(int,input().split()))
C.insert(0,0)

maxv = 0

for i in range(2,N+1):
    for j in range(int(i//2)+1):
        maxv = max(maxv,C[int(i-j)]+C[j])
    C[i] = maxv


print(C[N])