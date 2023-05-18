"""
    다익스트라 알고리즘을 사용한다. 이때 반대방향은 간선의 위치가 반대로 되어 만든다
"""

import sys
import heapq
input = sys.stdin.readline

# n : 정점 / m : 엑지 개수 / x : 목표정점
n, m, x = list(map(int,input().split()))
edge = [list(map(int,input().split())) for _ in range(m)]

maps = [[] for _ in range(n+1)]
r_maps = [[] for _ in range(n+1)] #간선방향이 반대인 배열

for item in edge:
    a = item[0]
    b = item[1]
    c = item[2]
    maps[a].append((b,c))
    r_maps[b].append((a,c))


#맵과 정점을 입력받아 각정점까지의 거리를 출력
def bfs(map, x):
    INF = float("inf")
    cntList = [INF] * (n+1) #x에서 각 인덱스로 가는 최소거리
    cntList[x] = 0
    visitList = [False] * (n+1)
    q = []
    heapq.heappush(q, (0, x))
    while q:
        ex = heapq.heappop(q)
        st = ex[1]

        visitList[st] = True

        for item in map[st]:
            if visitList[item[0]] == False:
                heapq.heappush(q,(min(cntList[item[0]], cntList[st]+item[1]),item[0]))
                cntList[item[0]] = min(cntList[item[0]], cntList[st]+item[1]) #기존값 vs 누적합+거리 중 더 큰값 리턴
    
    return cntList


xRange = bfs(maps,x) # x에서 각 정점 까지의 거리
#print(xRange)
r_xRnage = bfs(r_maps,x) # 각 정점에서 x까지의 거리
#print(r_xRnage)

maxv = 0
for i in range(1,n+1):
    maxv = max(maxv,xRange[i]+r_xRnage[i])

print(maxv)