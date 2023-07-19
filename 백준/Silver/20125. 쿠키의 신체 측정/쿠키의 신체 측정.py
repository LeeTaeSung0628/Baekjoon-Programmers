
import sys
input = sys.stdin.readline

n = int(input())

maps = [list(input().strip()) for _ in range(n)]

# 머리 찾기
def findHead(maps):
    head = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "*":
                head = [i,j]
                return head

def findWaist(x,y):
    #아래로 가능할때까지 이동
    cnt = 0
    while maps[x][y] == "*":
        cnt += 1
        x += 1
    return [x-1,y,cnt]

def findLeftArm(x,y):
    #왼쪽으로 가능할때까지 이동
    cnt = 0
    while maps[x][y] == "*":
        cnt += 1
        y -= 1
        if y < 0: break
    return cnt

def findRightArm(x,y):
    #오른쪽으로 가능할때까지 이동
    cnt = 0
    while maps[x][y] == "*":
        cnt += 1
        y += 1
        if y >= len(maps[0]): break
    return cnt

def findLeg(x,y):
    #아래로 가능할때까지 이동
    cnt = 0
    while maps[x][y] == "*":
        cnt += 1
        x += 1
        if x >= len(maps): break
    return cnt

            
head = findHead(maps)
heart = [head[0]+1,head[1]]
waist_x, waist_y ,waist = findWaist(heart[0]+1,heart[1])
leftArm = findLeftArm(heart[0],heart[1]-1)
rightArm = findRightArm(heart[0],heart[1]+1)
leftLeg =  findLeg(waist_x+1,waist_y-1)
rightLeg =  findLeg(waist_x+1,waist_y+1)

print(heart[0]+1,heart[1]+1)
print(leftArm,rightArm,waist,leftLeg,rightLeg)