
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

#상어칸에서 물고기 칸까지의 거리구하는 식
# = abs(sx - fx) + abs(sy - fy)

#1. 처음 상어 위치 구하기
shark = []
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] == 9:
            shark = [i,j]

#초기값
shark_size = 2
levelup = 2
time = 0

#넓이 우선탐색으로 물고기 탐색, 먹을 수 있는 물고기 탐색
# * 상 좌 우 하 순으로 탐색하며 가장 먼저 마주친 물고기가 범인이다
px = [-1,0,0,1]
py = [0,-1,1,0]

checkFish = True
while checkFish:
    check = [[False] * len(maps[0]) for _ in range(len(maps))]
    sx, sy = shark
    q = deque()
    q.appendleft([sx,sy,0])
    eatFish_list = []
    while q:
        x , y , nowdist= q.pop()

        for i in range(4):
            nx = x+px[i]
            ny = y+py[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and check[nx][ny] == False:
                if maps[nx][ny] == 0: #벽이면 탐색 진행
                    check[nx][ny] = True
                    q.appendleft([nx,ny,nowdist+1])

                elif 1 <= maps[nx][ny] < shark_size: #먹을 수 있는 고기면
                    if maps[nx][ny] != 9: #상어의 크기가 9가 넘어가면
                        check[nx][ny] = True
                        #현재위치가 아닌 상어위치와의 거리
                        dist = abs(sx-nx) + abs(sy-ny)
                        eatFish_list.append([nowdist+1,nx,ny])
                
                elif maps[nx][ny] == shark_size: #자신과 크기가 같으면 지나감
                    check[nx][ny] = True
                    q.appendleft([nx,ny,nowdist+1])
            
    if len(eatFish_list) == 0:
        checkFish = False
        continue #더이상 먹을 물고기가 없으면 끝

    #가장 가까운녀석들 중 우선순위높은애로 시식
    eatFish_list = sorted(eatFish_list, key= lambda x: (x[0],x[1],x[2]))

    #좌표바꾸기
    maps[sx][sy] = 0
    maps[eatFish_list[0][1]][eatFish_list[0][2]] = 9
    shark = [eatFish_list[0][1],eatFish_list[0][2]] 

    #이동한 시간 추가
    time += eatFish_list[0][0] #dist

    #레벨 업 까지 남은 물고기
    levelup -= 1
    if levelup == 0:
        shark_size += 1
        levelup = shark_size


print(time)


"""
3
0 0 1
2 0 0
0 9 0
"""