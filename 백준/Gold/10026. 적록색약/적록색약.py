
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(input().strip()) for _ in range(n)]

#일반인용 탐색
"""
아직 방문하지 않은 각 점에 대해서 모두 완전탐색한다.
"""
px = [0,0,1,-1]
py = [1,-1,0,0]
def bfs(x,y,st):
    q = deque()
    q.appendleft([x,y,st])
    while q:
        x, y ,my_st= q.pop()
        check[x][y] = True
        for p in range(4):
            nx = x + px[p]
            ny = y + py[p]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and check[nx][ny] == False:
                if my_st == "O": #색약색 이라면
                    if "R" == maps[nx][ny] or "G" == maps[nx][ny]:
                        q.appendleft([nx,ny,"O"])
                        check[nx][ny] = True
                else:
                    if my_st == maps[nx][ny]:
                        q.appendleft([nx,ny,maps[nx][ny]])
                        check[nx][ny] = True
    return 1


check = [[False] * len(maps[0]) for _ in range(len(maps))]
no_ans = 0 #일반인의 구역 개수
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if check[i][j] == False:
            no_ans += bfs(i,j,maps[i][j])


check = [[False] * len(maps[0]) for _ in range(len(maps))]
sy_ans = 0 #색약 구역 개수
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if check[i][j] == False:
            if maps[i][j] == "R" or maps[i][j] == "G":
                sy_ans += bfs(i,j,"O")
            else: sy_ans += bfs(i,j,maps[i][j])

print(no_ans,sy_ans)