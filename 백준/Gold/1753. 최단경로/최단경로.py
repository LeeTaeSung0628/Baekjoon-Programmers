"""
 해당 한 정점에서 다른 정점으로 가는 최단거리를 출력하라
"""
import heapq
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
start = int(input())
edge = [list(map(int,input().split())) for _ in range(m)]

#맵으로 만들기
INF = float("inf")
maps = [[] for _ in range(n)]
for item in edge:
    x, y, num = item
    maps[x-1].append([num,y-1])

check = [False] * n #재방문 방지 배열
#다익스트라 알고리즘 사용
q = [] #튜플 형태로 삽입시 0번째 값을 기준으로 우선순위 힙을 정한다.
heapq.heappush(q,(0,start - 1))
dist_arr = [INF] * n
while q:
    #우선순위가 가장높은것(방문가능한점 중 최단거리) pop
    dist , now = heapq.heappop(q)
    #방문처리
    check[now] = True
    if dist_arr[now] > dist: #최소값 갱신
        dist_arr[now] = dist
        #방문 가능한 지점 찾기
        for item in maps[now]:
            p_dist, p_now = item
            heapq.heappush(q, (dist+p_dist, p_now))
    else: continue

for d in dist_arr:
    if d == INF:
        print("INF")
    else:
        print(d)