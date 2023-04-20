# 시뮬레이션
import sys
input = sys.stdin.readline

N, M = map(int,input().split()) # N : map의 세로크기, M : map의 가로크기
r, c, d= map(int,input().split()) # r, c : 로봇의 초기 좌표, d : 바라보는 방향 0북/1동/2남/3서
map = [list(map(int,input().split())) * M for _ in range(N)]
chk = [[False] * M for _ in range(N)]
cnt = 0 #청소횟수
state = 1 #로봇청소기 작동 , 0이면 종료
dust = False #주변에 미청소구역이 있는지 체크

dy = [0,1,0,-1]
dx = [1,0,-1,0]
while state == 1:
    #현재칸이 청소되어있는지 체크 후 안되있으면 청소
    if chk[r][c] == False and map[r][c] == 0:
        chk[r][c] = True #청소
        cnt += 1

    #현재칸 주변 4칸에 청소되지 않은 칸 체크
    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        if 0<=ny<N and 0<=nx<M:
            if chk[ny][nx] == False and map[ny][nx] == 0: #하나라도 청소 안된곳이 있다면
                dust = True

    #하나라도 청소 안된곳이 있다면
    if dust == True:
        #왼쪽으로 90도 회전
        if d > 0:
            d -= 1
        else:
            d = 3

        #바라보는 앞쪽 칸 체크
        if d == 0 and 0<=(r-1)<N: # 북쪽 / 위칸 체크
            if(chk[r-1][c] == False and map[r-1][c] == 0): #청소가되어있지않고, 벽이 아니면
                r-=1 #한칸전진
        elif d == 1 and 0<=(c+1)<M: # 동쪽 / 오른쪽칸 체크 
            if(chk[r][c+1] == False and map[r][c+1] == 0): 
                c+=1 #한칸전진
        elif d == 2 and 0<=(r+1)<N: # 남쪽 / 아래칸 체크 
            if(chk[r+1][c] == False and map[r+1][c] == 0): 
                r+=1 #한칸전진
        elif d == 3 and 0<=(c-1)<M: # 서쪽 / 왼쪽칸 체크 
            if(chk[r][c-1] == False and map[r][c-1] == 0): 
                c-=1 #한칸전진

        dust = False

    #청소가 모두 되어있는경우
    else: 
        #바라보는 뒷쪽 칸 체크
        if d == 0 and 0<=(r+1)<N and map[r+1][c] == 0: # 북쪽 / 아래칸이 벽이 아니면
            r+=1 #한칸후진
        elif d == 1 and 0<=(c-1)<M and map[r][c-1] == 0: # 동쪽 / 아래칸이 벽이 아니면
            c-=1 #한칸후진
        elif d == 2 and 0<=(r-1)<N and map[r-1][c] == 0: # 남쪽 / 위칸이 벽이 아니면 
            r-=1 #한칸후진
        elif d == 3 and 0<=(c+1)<M and map[r][c+1] == 0: # 서쪽 / 오른쪽칸이 벽이 아니면
            c+=1 #한칸후진
        else: #후진할곳이 없다면 break
            state = 0 # 종료

print(cnt)