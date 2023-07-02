"""
   아이디어 : 3차원배열로 만든다! x, y, broken
"""
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [list(map(int,(input().strip()))) for _ in range(n)]

#누적 거리값(부셨는지 안부셨는지 포함)
distArr = [[[0] * m for _ in range(n)] for _ in range(2)]

q = deque()
q.append([0,0,0,1]) # x, y, broken ,dist
distArr[0][0][0] = 1
px = [1,-1,0,0]
py = [0,0,1,-1]
ans = []
reCheck = False
while q:
    broken, x, y, dist = q.popleft()
    
    if x == n-1 and y == m-1: # 끝점에 도달했다면 끝!
        ans = [broken,x,y,dist] 
        reCheck = True
        break

    #4방향 탐색
    for i in range(4):
        nx = x + px[i]
        ny = y + py[i]
        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
            #재방문 방지
            if distArr[broken][nx][ny] != 0:
                continue
            
            if maps[nx][ny] == 0: #갈수 있는 방향이고
                q.append([broken,nx,ny,dist+1])
                distArr[broken][nx][ny] = dist+1
            else:#벽일때,
                if broken == 0: #아직 벽을 깰 수 있다면!?
                    q.append([1,nx,ny,dist+1])
                    distArr[1][nx][ny] = dist+1
if reCheck == False:
    print(-1)
else:
    print(ans[3])


