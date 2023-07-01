"""
   아랫 수
    dp를 이용해서, 다음 칸에 올수있는 최대점수, 최소 점수를 저장시킨다.
"""

import sys
input = sys.stdin.readline
n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]

#최대 최소 dp 배열 2줄짜리
maxdp = [[0,0,0] for _ in range(2)]
mindp = [[0,0,0] for _ in range(2)]

#첫 줄 s로 초기화
maxdp[0] = s[0].copy()
mindp[0] = s[0].copy()

for t in range(1,n):
    #1 부터 시작해서, 0 ,1 ,0, 1 반복..
    i=t%2

    #i = 0일떄, -1은 마지막배열(1)을 가리킨다.
    #i = 1일때, i-1은 0이다.
    mindp[i][0] = min(mindp[i-1][0] +s[t][0],mindp[i-1][1] +s[t][0])
    mindp[i][1] = min(mindp[i-1][0] +s[t][1],mindp[i-1][1] +s[t][1],mindp[i-1][2]+s[t][1])
    mindp[i][2] = min(mindp[i-1][1] +s[t][2],mindp[i-1][2] +s[t][2]) 

    maxdp[i][0] = max(maxdp[i-1][0] +s[t][0],maxdp[i-1][1] +s[t][0])
    maxdp[i][1] = max(maxdp[i-1][0] +s[t][1],maxdp[i-1][1] +s[t][1],maxdp[i-1][2]+s[t][1])
    maxdp[i][2] = max(maxdp[i-1][1] +s[t][2],maxdp[i-1][2] +s[t][2])

print(max(maxdp[n%2-1]),min(mindp[n%2-1]))