
import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
if maps[0][1] > 0: #건물이 있다면
    stack = [maps[0][1]]
    cnt = 1
else:
    stack = [0]
    cnt = 0

for i in range(1,len(maps)):
    anum = maps[i][1]

    #현재값이최고 높이보다 크면 삽입하고 카운트(비어있으면 삽입)
    if len(stack) == 0:
        stack.append(anum)
        cnt += 1
        continue

    if anum > stack[-1]:
        stack.append(anum)
        cnt += 1
        continue
    
    #현재값이 최고높이보다 작으면 그높이까지 pop
    while anum < stack[-1]:
        stack.pop()
        if len(stack) == 0:#더 낮아지면, 삽입하고 카운트(0이 아닐때)
            break

    #마지막높이가 자신과 같으면 이미있는건물, 아니면 새로운 더 낮은건물
    if len(stack) == 0:
        if anum != 0:
            stack.append(anum)
            cnt += 1
    else:
        if stack[-1] != anum:
            stack.append(anum)
            cnt += 1

print(cnt)
