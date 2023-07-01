"""
   트리 지름 구하기(가장 긴 거리) 

   루트 노드를 기준으로 너비우선 탐색을 한다.
   가중치가 가장 높은 노드를 기준으로 다시 한 번 너비우선 탐색을 한다.
   이때 최대 가중치가 지름이다...

"""

import sys
input = sys.stdin.readline

n = int(input())
tree = [list(map(int,input().split())) for _ in range(n-1)]

#맵 만들기
maps = [[] for _ in range(n)]
for item in tree:
    st, en, num = item
    maps[st-1].append([en-1, num])
    maps[en-1].append([st-1, num])

#가장 긴 길이 탐색
def bfs(start, maps):
    visit = [False] * n
    max_dist = [0,0]
    q = []
    q.append([0, start])
    while q:
        dist, now = q.pop()
        visit[now] = True
        if max_dist[1] < dist:
            max_dist = [now, dist]

        for nextValue in maps[now]:
            next, n_dist = nextValue
            if visit[next] == False:
                q.append([dist+n_dist, next])
    return max_dist
        

max_val = bfs(0,maps)
ans = bfs(max_val[0],maps)
print(ans[1])



