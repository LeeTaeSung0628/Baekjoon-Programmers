"""
아이디어 : 1. 배열의 길이가 4인 정점(맨끝값)을 기준으로 가장 긴 길이를 구하고 저장한다.
            1.1 한 정점을 선택한 후, 해당 정점과 연결되어 있는 정점으로 방문, 방문시 가지고있던 값 + 이동하는데 든 값을 더해서 넘겨준다.
                q.append([방문할 정점,현재까지 누적비용 + 이동비용])
         2. 이때 방문했던 모든 정점은 재방문 할 수 있지만, 맨끝값으로 선정될 수는 없다.( 안구해도됨. )
         3. 이렇게 구한 길이 중 가장 긴것이 정답이다.
"""

import sys
import heapq

input = sys.stdin.readline

n = int(input()) # 정점의 개수
edge = [list(map(int,input().split())) for _ in range(n)]

#시작부분이 될 길이가 4인배열들의 set
startPoint = []
for item in edge:
    if len(item) == 4:
        startPoint.append(item[0])
startPoint = set(startPoint)

#edge를 기반으로 만든 map
maps = [0] * n
for i in range(len(edge)):
    ex = [] #임시저장배열
    for j in range(1,len(edge[i])-1,2):
        ex.append(edge[i][j])
        ex.append(edge[i][j+1])
    maps[edge[i][0]-1] = ex

res = []
q = []
heapq.heappush(q,[1,0])
check_maps = [False] * n #재방문 방지
check_maps[0] = True

while q:
    chck_push = False #끝까지 도달했는지

    item = heapq.heappop(q) #큐에서 요소 꺼내기
    start = item[0]
    c = item[1]
    check_maps[start-1] = True
    
    for j in range(0,len(maps[start-1]),2):
        if check_maps[maps[start-1][j] - 1] == False:
            chck_push = True
            heapq.heappush(q, [maps[start-1][j], c + maps[start-1][j+1]])

    if chck_push == False:
        res.append([start,c])

res = sorted(res, key=lambda x : x[1],reverse=True)

#  "====================================="

res2 = []
q2 = []
heapq.heappush(q2,[res[0][0],0]) #최대길이를 찾은값으로 다시 탐색
check_maps2 = [False] * n #재방문 방지
check_maps2[res[0][0]-1] = True
while q2:
    chck_push = False #끝까지 도달했는지

    item = heapq.heappop(q2) #큐에서 요소 꺼내기
    start = item[0]
    c = item[1]
    check_maps2[start-1] = True
    
    for j in range(0,len(maps[start-1]),2):
        if check_maps2[maps[start-1][j] - 1] == False:
            chck_push = True
            heapq.heappush(q2, [maps[start-1][j], c + maps[start-1][j+1]])

    if chck_push == False:
        res2.append([start,c])

res2 = sorted(res2, key=lambda x : x[1],reverse=True)


if res[0][1] == res2[0][1]:
    print(res[0][1])
else:
    print(max(res[0][1],res2[0][1]))


