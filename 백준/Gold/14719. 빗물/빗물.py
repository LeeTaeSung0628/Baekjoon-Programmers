import sys
input = sys.stdin.readline

"""
아이디어 : 가로로 이동하면서, 1을 발견하고 다음 1을 발견할때까지 0의 개수를 센다. 그것이 막힌 칸 이니까..
        벽으로 끝나야 벽이다.!
"""

h , w = map(int,input().split())
bb = list(map(int,input().split()))
maps = [[0] * w for _ in range(h)]

for i in range(len(maps)):#높이별
    for j in range(len(maps[0])): #넓이별
        if bb[j] >= len(maps)-i:
            maps[i][j] = 1

cnt = 0
for i in range(len(maps)):#높이별
    check_wall = False #벽과 벽 사이인지?
    temp = 0 #임시 카운트
    for j in range(len(maps[0])): #넓이별
        #벽을 발견하면 다음벽까지 수를 센다.
        if maps[i][j] == 1: #현재 상태를 벽안인지 벽 밖인지 체크
            if check_wall == True:  #벽이었다가 다시 닫혔을떄! 카운트 추가
                cnt += temp
                temp = 0
            else:
                check_wall = True
        
        if maps[i][j] == 0 and check_wall == True:
            temp+=1

        
print(cnt)