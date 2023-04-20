import sys
input = sys.stdin.readline

N = int(input())
pointList = [list(map(int,input().split())) for _ in range(N)]
sortList = [[int] * 2 for _ in range(N)]
minv = pointList[0]

pointList.sort()

for i in range(N):
    print(pointList[i][0],pointList[i][1])