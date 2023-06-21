import sys
input = sys.stdin.readline

"""
    1. 모든 비어있는 칸에 대해서 구한다
        1.1 해당학생이 좋아하는 학생의 번호가 가장많이 인접한 칸
         1.1.1 해당칸이 여러개 일때, 그 칸에대해서 비어있는 인접한 칸개수 세기
            1.1.1.1 인접한 칸의 개수가 한개 이상일때, 행, 열 순으로 오름차순
"""

#교실 크기
n = int(input())
#학생별 선호 인
love = [list(map(int, input().split())) for _ in range(n**2)]
#교실 맵
maps = [[0] * n for _ in range(n)]

px = [0,1,0,-1]
py = [1,0,-1,0]


#빈칸이면서 내가 좋아하는학생이 인접한 수, 빈칸의 개수 세기
for person in love:
    res = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 0: #해당칸이 비어있으면:
                null_cnt = 0
                love_cnt = 0
                for m in range(4):
                    nx = i+px[m]
                    ny = j+py[m]
                    if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                        if maps[nx][ny] == 0:
                            null_cnt += 1
                        for p in range(1,len(person)):
                            if person[p] == maps[nx][ny]:
                                love_cnt += 1
                res.append([i,j,love_cnt,null_cnt])
    res = sorted(res, key=lambda x: (-x[2],-x[3],x[0],x[1]))
    maps[res[0][0]][res[0][1]] = person[0]

cnt = 0 #만족도
love = sorted(love, key=lambda x: (x[0]))
for i in range(len(maps)):
    for j in range(len(maps[0])):
        love_cnt_last = 0
        for m in range(4):
            nx = i+px[m]
            ny = j+py[m]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                for p in love[maps[i][j]-1]:
                    if p == maps[nx][ny]:
                        love_cnt_last += 1
        if love_cnt_last == 1:
            cnt += 1
        elif love_cnt_last == 0:
            cnt += 0
        else: cnt += 10**(love_cnt_last-1)

print(cnt)