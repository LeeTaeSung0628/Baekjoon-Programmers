import sys
input = sys.stdin.readline

"""
    맡닿아있는 인덱스 수는 이전바퀴가 있을때, 자신의 7번과 이전바퀴의 3번
                    다음바퀴가 있을때, 자신의 3번과 다음바퀴의 7번 이 서로 상호작용한다

                    만약 n번째바퀴가 회전할때 자신의 7번과, n-1의 3번이 다르다면 회전시킨다.
                                자신의 3번과 n+1의 7번이 다르다면 회전시킨다. (반복)
"""

gear = [list(map(int,list(input().strip()))) for _ in range(4)]
n = int(input())
spin = [list(map(int,input().split())) for _ in range(n)]

def spin_gear(n,upDown,visit):
    visit[n] = True
    
    if n-1 >= 0 : #이전 톱니가 존재하면
        if gear[n][6] != gear[n-1][2] and visit[n-1] == False:
            if upDown == 1: spin_gear(n-1,-1,visit)
            else: spin_gear(n-1,1,visit)
    if n+1 < 4: #다음 톱니가 존재하면
        if gear[n][2] != gear[n+1][6] and visit[n+1] == False:
            if upDown == 1: spin_gear(n+1,-1,visit)
            else: spin_gear(n+1,1,visit)
    
    if upDown == 1: #시계방향
        #톱니 회전시키기
        temp = gear[n].pop()
        gear[n].insert(0,temp)
    else: #반시계방향
        temp = gear[n].pop(0)
        gear[n].append(temp)

for item in spin:
    visit = [False] * 4
    spin_gear(item[0]-1,item[1],visit)

score = 0
#점수구하기
for i in range(len(gear)):
    if gear[i][0] == 1: #s극이면
        score += 2**i

print(score)