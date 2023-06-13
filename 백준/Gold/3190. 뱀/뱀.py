import sys
input = sys.stdin.readline

"""
 1. 뱀이 벽이나 자기자신에게 부딛힐때까지 무한반복!
  사과위치를 맵핑하고 매 칸마다 체크해준다.
"""

n = int(input())
a = int(input())
app = [list(map(int,input().split())) for _ in range(a)]
b = int(input())
bam = [list(input().split()) for _ in range(b)]

#맵 만들기
maps = [[0] * n for _ in range(n)]
for item in app:
        maps[item[0]-1][item[1]-1] = 1

#[0] => 오른쪽이동 / [1] => 아래이동 / [2] => 왼쪽이동 / [3] => 위로이동
nx = [0,1,0,-1]
ny = [1,0,-1,0]

# 현재 뱀이 바라보는 상태
state = 0
# 현재 뱀 머리 위치
h_x = 0
h_y = 0
#다음 꼬리위치 q
q = []
q.insert(0,[0,0])
# 현재 시간
time = 0
#몇번째 이동인지
b_cnt = 0

maps[h_x][h_y] = 3
while True:
    time += 1
    h_x = h_x+nx[state]
    h_y = h_y+ny[state]
    q.insert(0,[h_x,h_y])
    #다음칸으로 진행 가능하다면
    if 0 <= h_x < n and 0 <= h_y < n and maps[h_x][h_y] != 3:
        if maps[h_x][h_y] == 0:#사과가 아니면
            item = q.pop()
            t_x = item[0]
            t_y = item[1]
            maps[t_x][t_y] = 0 #꼬리 한칸 줄이기
            maps[h_x][h_y] = 3
        else: #사과면
            maps[h_x][h_y] = 3

        if len(bam) > b_cnt and int(bam[b_cnt][0]) == time: #동작이 끝날때 회전
            if bam[b_cnt][1] == "L":
                if state > 0: state -= 1
                else: state = 3
                b_cnt+=1
            else:
                if state < 3: state += 1
                else: state = 0
                b_cnt+=1

    else:
        ans = time
        break

print(ans)