import sys
input = sys.stdin.readline

N = int(input())
pointList = [list(map(int,input().split())) for _ in range(N)]

pointList.sort(key= lambda x : (x[1], x[0]))

for i in range(N):
    print(pointList[i][0],pointList[i][1])