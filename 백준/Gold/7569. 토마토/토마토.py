
import sys
from collections import deque
input = sys.stdin.readline

m, n ,h = map(int,input().split())
maps = [list([list(map(int,input().split())) for _ in range(n)]) for _ in range(h)]

px = [0,0,0,0,1,-1]
py = [0,0,1,-1,0,0]
ph = [1,-1,0,0,0,0]

#처음 후숙과일 위치 찾기

def mainSolution():
    hoosook = []
    checkOne = False #하나라도 익지 않은게 있는지 체크
    for z in range(h):
        for i in range(n):
            for j in range(m):
                if maps[z][i][j] == 1:
                    hoosook.append([z,i,j])
                elif maps[z][i][j] == 0:
                    checkOne = True

    if checkOne == False:
        return 0 #모두익어있다면 0

    #주변으로 숙성을 퍼트리는 과정
    cnt = 0
    checkAll = True #한번이라도 전염 시켰는지 체크
    while checkAll:
        checkAll = False
        temp = [] #임시 저장 배열
        while hoosook:
            my_h,my_x,my_y = hoosook.pop()

            for p in range(6):
                nh = my_h + ph[p]
                nx = my_x + px[p]
                ny = my_y + py[p]
                #범위를 벗어나지 않고,
                if 0 <= nh < len(maps) and 0 <= nx < len(maps[0]) and 0 <= ny < len(maps[0][0]):
                    #익지 않은 토마도가 있다면
                    if maps[nh][nx][ny] == 0:
                        maps[nh][nx][ny] = 1
                        temp.append([nh,nx,ny])
                        checkAll = True #하나라도 익은게 있는지 체크

        hoosook = temp.copy()
        cnt += 1


    #처리 후에도 안익은 과일이 있나 체크
    checkLast = False
    for z in range(h):
        for i in range(n):
            for j in range(m):
                if maps[z][i][j] == 0:
                    checkLast = True
    
    if checkLast: return -1
    else: return cnt-1

print(mainSolution())
