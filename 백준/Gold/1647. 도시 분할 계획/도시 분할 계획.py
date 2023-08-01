
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
edge = [list(map(int,input().split())) for _ in range(M)]

#최소 스패닝 트리 ( 사이클이 발생하지 않는 최소 간선)
# -> 유니온 파인드로 구한다( 크루스칼 알고리즘 )
"""
1. 간선을 작은순으로 정렬한다
2. 현재 간선이 사이클을 발생시키는지 확인한다(같은 부모인지 find)
2.1 발생시키지 않는다면 최소신장트리에 포함(유니온)시킨다
2.2 발생시키면 포함시키지 않는다
"""
#부모찾기
def find(parent, x):
    #부모가 자기 자신이라면 리텃
    if parent[x] == x:
        return x
    else:
        return find(parent, parent[x])

#같은 부모로 만들기
def union(rank,parent, x, y):
    xp = find(parent, x)
    yp = find(parent, y)

    #xp가 더 큰 집합이면 xp를 부모로
    if rank[xp] > rank[yp]:
        parent[yp] = xp
    elif rank[xp] < rank[yp]:
        parent[xp] = yp
    else:
        parent[yp] = xp
        rank[xp] += 1
    
    
parent = [[] for _ in range(N+1)]
rank = [0] * (N+1)
#모든 부모를 자기자신으로 초기화
for i in range(1,N+1):
    parent[i] = i

#비용이 낮은 순서로 정렬
edge = sorted(edge, key=lambda x : x[2])

total = 0
maxdist = 0
for item in edge:
    x, y, dist = item
    #부모가 같다면(싸이클이 생긴다)
    if find(parent, x) == find(parent, y):
        continue
    else:
        #부모가 다르면 합치고, 거리 추가
        last = dist
        union(rank,parent,x, y)
        total += dist

print(total - last)