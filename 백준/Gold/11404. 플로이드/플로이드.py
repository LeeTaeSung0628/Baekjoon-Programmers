

import sys
input = sys.stdin.readline

"""
플로이드 워셜 알고리즘
모든 정점에 대해 다른 모든 정점까지의 거리 구하기
"""

n = int(input())
e = int(input())
edge = [list(map(int,input().split())) for _ in range(e)]

#맵 만들기
inf = 100000*100000
maps = [[inf] * n for _ in range(n)]
for i in range(len(maps)):
    maps[i][i] = 0
for item in edge:
    s , e , dist = item
    maps[s-1][e-1] = min(dist,maps[s-1][e-1])
"""
플로드이드 워셜 점화식 : 시작점->끝점 = min(시작점->끝점 ,  시작점->거처가는점->끝점)
"""
#거쳐가는 정점
for x in range(n):
    # Startingpoint
    for y in range(n):
        # Endpoint
        for z in range(n):
            if maps[y][x] == inf or maps[x][z] == inf:
                continue
            maps[y][z] = min(maps[y][z], maps[y][x] + maps[x][z])

for i in range(n):
    for j in range(n):
        if maps[i][j] == inf:
            print('0 ', end="")
        else:
            print(maps[i][j], end=" ")
    print("")