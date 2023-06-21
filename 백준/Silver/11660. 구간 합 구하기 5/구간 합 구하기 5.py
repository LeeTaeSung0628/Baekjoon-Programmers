import sys
input = sys.stdin.readline

"""
아이디어 : (2,3)~(4,5) => 2,3/2,4/2,5
                        3,3,3,4,,,
                        4,3,.
이때, 2,3 ~ 2,5 까지 구할때 누적합테이블에서 2,5 - (2,5 - 2,3)을 한다~
"""

# n 표의크기 / m 문제개수
n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
qe = [list(map(int,input().split())) for _ in range(m)]

#가로 누적합 테이블 만들기
for i in range(len(maps)):
    temp = 0
    for j in range(len(maps[0])):
        maps[i][j] = maps[i][j]+temp
        temp = maps[i][j]

#세로 누적합 테이블 만들기
for j in range(len(maps[0])):
    temp = 0
    for i in range(len(maps)):
        maps[i][j] = maps[i][j]+temp
        temp = maps[i][j]

cnt = 0
for item in qe:
    cnt = 0
    x1,y1,x2,y2 = item
    x1 = x1-1
    y1 = y1-1
    x2 = x2-1
    y2 = y2-1
    #누적값 - ((왼쪽 영역 + 위쪽영역) - 대각선영역)
    p1 = 0
    p2 = 0
    p3 = 0
    if y1-1 >= 0:
        p1 = maps[x2][y1-1]
    if x1-1 >= 0:
        p2 = maps[x1-1][y2]
    if x1-1 >= 0 and y1-1 >= 0:
        p3 = maps[x1-1][y1-1]
    cnt += maps[x2][y2] - ((p1 + p2) - p3)
    print(cnt)