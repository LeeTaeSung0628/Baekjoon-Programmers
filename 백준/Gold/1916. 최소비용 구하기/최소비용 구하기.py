import sys
import heapq
input = sys.stdin.readline

# n정점의 개수
n = int(input())
# m간선 개수
m = int(input())
edge = [list(map(int,input().split())) for _ in range(m)]
start , end = map(int,input().split())

"""
다익스트라 알고리즘을 사용한다
"""
#맵 생성
maps = [[] for _ in range(n)]
for item in edge:
    st, en , num = item
    maps[st-1].append([en-1,num])

INF = int(10**10)
distArr = [INF] * n
q = []
heapq.heappush(q, (0,start-1))
while q:
    dist, now = heapq.heappop(q)

    if distArr[now] > dist:
        distArr[now] = dist
        for item in maps[now]:
            next, next_dist = item
            heapq.heappush(q,(dist+next_dist, next))
print(distArr[end-1])
