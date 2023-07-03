"""


"""
import sys
input = sys.stdin.readline

n = int(input()) # 피라미드 높이
maps = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n): #맨위 꼭짓점 부터
    for j in range(len(maps[i])):
        if j == 0: maps[i][j] += maps[i-1][j]
        elif j == len(maps[i])-1: maps[i][j] += maps[i-1][j-1]
        else: maps[i][j] += max(maps[i-1][j],maps[i-1][j-1])

print(max(maps[-1]))