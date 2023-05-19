"""
    1번 노드에서 u번 노드 -> v번 노드 -> N번노드 가 최단거리 일 수 있고,
    1번 노드에서 v번 노드 -> u번 노드 -> N번노드 가 최단거리 일 수 있다

    다익스트라 알고리즘을 이용하여 해당노드에서 방문할수 있는 노드들의 가장 짧은 루트를 구할 수 있다.
    u와 v 두개를 구한다.

    1번 케이스 : u에서 1까지 + u에서 v까지 + v에서 N까지
    2번 케이스 : v에서 1까지 + v에서 u까지 + u에서 N까지
    
    두 개의 케이스 중 최단 거리를 구하면 정답!
"""

import sys
import heapq
input = sys.stdin.readline

N, E = list(map(int,input().split()))

maps = [[] for _ in range(N+1)]
for _ in range(E):
    item = list(map(int,input().split()))
    a = item[0]
    b = item[1]
    c = item[2]
    maps[a].append((b, c))
    maps[b].append((a, c))
    
u, v = list(map(int,input().split()))

def djicstra(maps,x): #맵과 출발정점
    #방문여부탐색
    visit = [False] * len(maps)
    #누적최단거리
    INF = float("inf")
    distList = [INF] * len(maps)

    q = []
    heapq.heappush(q, (0,x)) # 우선순위큐(최단거리순)
    distList[x] = 0
    while q:
        item = heapq.heappop(q)
        dist = item[0]
        now = item[1]
        visit[now] = True #방문처리

        for node in maps[now]:
            #node[0] = 이동할 노드 / node[1] = 이동하는데 드는 비용
            if visit[node[0]] == False:
                if distList[node[0]] > dist + node[1]: #min(기존값, 누적값 + 움직이는값)
                    heapq.heappush(q, (dist + node[1], node[0]))
                    distList[node[0]] = dist + node[1] #여기서 안넣고 팝 이후에 넣게된다면, 매번 최소값이 갱신될수 없음(한번만 실행되기 때문에)

                else:
                    continue

    return distList

uMaps = djicstra(maps,u)
vMaps = djicstra(maps,v)

"""
    1번 케이스 : u에서 1까지 + u에서 v까지 + v에서 N까지
    2번 케이스 : v에서 1까지 + v에서 u까지 + u에서 N까지
"""
case1 = uMaps[1] + uMaps[v] + vMaps[N]
case2 = vMaps[1] + vMaps[u] + uMaps[N]

if case1 == float("inf") or case2 == float("inf"):
    print(-1)
else:
    print(min(case1,case2))
