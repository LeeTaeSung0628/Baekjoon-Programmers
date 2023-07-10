"""
Qeen을 서로 죽이지 못하게 놓는 방법

"""

import sys
input = sys.stdin.readline

n = int(input())

#맵 만들기
maps = [[0] * n for _ in range(n)]

ans = 0
v1 = [0] * (n+1) # 내위에 있는지( j값이 같으면 x ) 0 ~ n
v2 = [0] * (n * 2 + 1) # 오른쪽 대각선( i + j 값이 같으면 x ) 0 ~ n*2
v3 = [0] * (n * 2 + 1) # 왼쪽 대각선 ( i - j 값이 같으면 ) -n ~ n
def dfs(o_maps,i,o_v1,o_v2,o_v3):

    global ans
    
    maps = o_maps.copy()
    v1 = o_v1.copy()
    v2 = o_v2.copy()
    v3 = o_v3.copy()

    if i == n:
        ans += 1
        return
    checkF = False
    for j in range(len(maps)):
        if v1[j] == 0:
            if v2[i+j] == 0:
                if i-j < 0: #음수면
                    if v3[i-j + n] == 0:
                        if maps[i][j] == 0:
                            checkF = True
                            maps[i][j] = 1
                            v1[j] = 1
                            v2[i+j] = 1
                            v3[i-j + n] = 1
                            dfs(maps,i+1,v1,v2,v3)
                            v1[j] = 0
                            v2[i+j] = 0
                            v3[i-j + n] = 0
                            maps[i][j] = 0
                else:
                    if v3[i-j + n] == 0:
                        if maps[i][j] == 0:
                            checkF = True
                            maps[i][j] = 1
                            v1[j] = 1
                            v2[i+j] = 1
                            v3[i-j + n] = 1
                            dfs(maps,i+1,v1,v2,v3)
                            v1[j] = 0
                            v2[i+j] = 0
                            v3[i-j + n] = 0
                            maps[i][j] = 0
        
dfs(maps,0,v1,v2,v3)   

print(ans)