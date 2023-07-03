"""
    내부에 있는 빈칸인지 체크해야한다.
    0,0으로 시작하여, 외부의 공기를 전부체크한다. 100
    
    모든치즈개수에 대하여 동서남북에 외부공기가 2개 이사인지 체크한다. 40000

    모든치즈가 사라질때까지 반복한다. 1000번정도 => 불가능

    0,0부터 시작해서 외부공기를 전부체크할때, 치즈 위치를 따로 저장한다.
    
    체크한 치즈들에 대해서만 외부공기에 2개이상 노출되었는지 체크한다.

    모든 치즈가 사라질 떄 까지 반복한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

px = [1,-1,0,0]
py = [0,0,1,-1]
checkFinal = True # 녹일 치즈가 없으면 끝
cnt = 0
while checkFinal:
    checkFinal = False
    #외부 공기 좌표 저장
    airMaps = [[1] * m for _ in range(n)]
    #외부 공기 위치 저장(내부 공기와 따로 체크하기 위함.)
    q = deque()
    q.appendleft([0,0]) # x,y

    while q:
        x, y = q.pop()

        for i in range(4):
            nx = x + px[i]
            ny = y + py[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 0: #공기이고
                    if airMaps[nx][ny] == 1: #아직방문 안했으면
                        q.append([nx,ny])
                        airMaps[nx][ny] = 0

    #외부 공기에 대해서 동서남북으로 count하여 2 이상인 치즈를 없앰다
    for x in range(len(airMaps)):
        for y in range(len(airMaps[0])):
            if airMaps[x][y] == 0:
                for p in range(4):
                    nx = x + px[p]
                    ny = y + py[p]
                    if 0 <= nx < len(airMaps) and 0 <= ny < len(airMaps[0]):
                        if airMaps[nx][ny] == 1: #처음노출되는것 이면
                            airMaps[nx][ny]+=1
                        elif airMaps[nx][ny] == 2:
                            airMaps[nx][ny]+=1
                            maps[nx][ny] = 0 #두번노출되면 녹아서 사라짐
                            checkFinal = True #한번도 못 녹이면 False 상태
            else: continue

    cnt += 1

print(cnt - 1)

"""
9 9
0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0
0 1 0 0 0 0 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 0 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0
"""