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
        
for item in qe:
    cnt = 0
    x1,y1,x2,y2 = item
    x1 = x1-1
    y1 = y1-1
    x2 = x2-1
    y2 = y2-1

    for x in range(x1,x2+1):
        com = 0
        if y1-1 >= 0:
            com = (maps[x][y1-1]) #0이하면 안빼도 됨
        cnt += maps[x][y2] - com
    print(cnt)