"""
최소 몇번만에 구슬을 빼낼 수 있을지
아이디어 : 기울이기의 4가지 동작 => 빨간구슬과 파란구슬이 해당 동,서,남,북 맨끝으로 이동한다.
        dfs로 진행한다. 4가지의 경우 4^10 = 100만
"""

import sys
import copy
input = sys.stdin.readline

def dfs(maps,cnt,red,blue,nesw):
    global res

    if cnt > 10:
        return res.append(11)

    maps = copy.deepcopy(maps)
    red = red.copy()
    orx = red[0] #원래위치
    ory = red[1]
    rx = red[0]
    ry = red[1]
    blue = blue.copy()
    obx = blue[0]
    oby = blue[1]
    bx = blue[0]
    by = blue[1]
  
    ckR_goal = False #골인했는지
    ckB_goal = False

    #동서남북으로 이동 
    while nesw != "X":
        ckRed = False #벽에 닿았는지
        ckBlue = False #둘다 벽에 닿으면 정지

        if nesw == "N": #북쪽으로 계속이동 x가 -1 씩이동
            if maps[rx-1][ry] == 1: #빨간공 이동
                maps[rx][ry] = 1
                rx-=1
                maps[rx][ry] = 2
            elif maps[rx-1][ry] == 9:
                ckR_goal = True
                ckRed = True
                maps[rx][ry] = 1
            else:
                ckRed = True

            if maps[bx-1][by] == 1: #파란공이동
                maps[bx][by] = 1
                bx-=1
                maps[bx][by] = 3
            elif maps[bx-1][by] == 9:
                ckB_goal = True
                ckBlue = True
                maps[bx][by] = 1
            else:
                ckBlue = True
            
            if ckRed == True and ckBlue == True: #둘다 벽이면 정지
                break

        if nesw == "E": #동쪽으로 계속이동 y가 +1 씩 이동
            if maps[rx][ry+1] == 1:
                maps[rx][ry] = 1
                ry+=1
                maps[rx][ry] = 2
            elif maps[rx][ry+1] == 9:
                ckR_goal = True
                ckRed = True
                maps[rx][ry] = 1
            else:
                ckRed = True
            if maps[bx][by+1] == 1:
                maps[bx][by] = 1
                by+=1
                maps[bx][by] = 3
            elif maps[bx][by+1] == 9:
                ckB_goal = True
                ckBlue = True
                maps[bx][by] = 1
            else:
                ckBlue = True
            
            if ckRed == True and ckBlue == True:
                break
         
        if nesw == "S": #남쪽으로 계속이동 x가 +1 씩 이동
            if maps[rx+1][ry] == 1:
                maps[rx][ry] = 1
                rx+=1
                maps[rx][ry] = 2
            elif maps[rx+1][ry] == 9:
                ckR_goal = True
                ckRed = True
                maps[rx][ry] = 1
            else:
                ckRed = True
            if maps[bx+1][by] == 1:
                maps[bx][by] = 1    
                bx+=1
                maps[bx][by] = 3
            elif maps[bx+1][by] == 9:
                ckB_goal = True
                ckBlue = True
                maps[bx][by] = 1
            else:
                ckBlue = True
            
            if ckRed == True and ckBlue == True:
                break

        if nesw == "W": #서쪽으로 계속이동 y가 -1 씩 이동
            if maps[rx][ry-1] == 1:
                maps[rx][ry] = 1
                ry-=1
                maps[rx][ry] = 2
            elif maps[rx][ry-1] == 9:
                ckR_goal = True
                ckRed = True
                maps[rx][ry] = 1
            else:
                ckRed = True
            if maps[bx][by-1] == 1:
                maps[bx][by] = 1
                by-=1
                maps[bx][by] = 3
            elif maps[bx][by-1] == 9:
                ckB_goal = True
                ckBlue = True
                maps[bx][by] = 1
            else:
                ckBlue = True
            
            if ckRed == True and ckBlue == True:
                break

    if ckR_goal == True and ckB_goal == False: #골인시 체크
        return res.append(cnt)
    elif ckR_goal == False and ckB_goal == True:
        return
    elif ckR_goal == True and ckB_goal == True:
        return  

    red = []
    blue = []
    red.append(rx)
    red.append(ry)
    blue.append(bx)
    blue.append(by)
 
    px = [-1,0,1,0]
    py = [0,1,0,-1]
    ps = ["N","E","S","W"]
    chk = ["S","W","N","E"] #왔던방향 탐색 막기
    for i in range(4):
        rnx = rx+px[i]
        rny = ry+py[i]
        bnx = bx+px[i]
        bny = by+py[i]
        if (maps[rnx][rny] != 0 or maps[bnx][bny] != 0) and chk != nesw: #ex: nesw="N" 일때 S로 못가게함
            dfs(maps,cnt+1,red,blue,ps[i])
             
#n : 세로 / m : 가로
n,m = map(int,input().split())
maps = [input().strip() for _ in range(n)]

#빨간구슬, 파란구슬 위치 알아내기
red = []
blue = []

# 맵 숫자로 맵핑
newMaps = [[0] * m for _ in range(n)]
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] == "R":
            red.append(i)
            red.append(j)
            newMaps[i][j] = 2
        elif maps[i][j] == "B":
            blue.append(i)
            blue.append(j)
            newMaps[i][j] = 3
        elif maps[i][j] == "#":
            newMaps[i][j] = 0
        elif maps[i][j] == ".":
            newMaps[i][j] = 1
        elif maps[i][j] == "O":
            newMaps[i][j] = 9

res = []        
   
dfs(newMaps,0,red,blue,"X")

ans = min(res)

if ans == 11:
    print(-1)
else:
    print(min(res))