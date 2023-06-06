import sys
from itertools import combinations
import copy
input = sys.stdin.readline

#가스 채우기
def gasal(maps):
    maps = copy.deepcopy(maps)

    gas = []
    #독까스 탐색
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == 2:
                gas.append([x,y])

    #가스 살포
    px = [0,1,0,-1]
    py = [1,0,-1,0]
    while gas:
        q = []
        q.append(gas.pop())
        while q:
            x, y = q.pop()

            for n in range(4):
                nx = x+px[n]
                ny = y+py[n]

                if 0 <= nx < len(maps)  and 0 <= ny < len(maps[0]) and maps[nx][ny] == 0:
                    maps[nx][ny] = 2
                    q.append([nx,ny])

    cnt = 0

    #살포 후 살아남은 공간 탐색
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == 0:
                cnt+=1
    
    return cnt

#막대기가 놓일 수 있는 경우의 수
n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

items = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            items.append([i,j])
# c = 막대기가 놓일 수 있는 경우의 수
c_list = list(combinations(items,3))


res = []
for c in c_list:
    #맵 초기화
    c_maps = copy.deepcopy(maps)
    
    #벽 세우기
    for item in c:
        c_maps[item[0]][item[1]] = 1

    #가스처리
    res.append((gasal(c_maps)))

print(max(res))