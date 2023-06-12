from itertools import combinations
from itertools import permutations

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

chick = []
count = 1
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] == 2:
            chick.append((i,j,count))
            count+=1

com = []
for i in range(1,count):
    com.append(i)

chick_com = list(combinations(com,m))

#사용가능한 치킨집만큼만 사용(남길 치킨집개수 m)

ans_list = []    

for chick_com_item in chick_com:
    ans = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1: #모든집에 대하여 어느치킨집이 가장 작은지

                min_dist = 999999
                for c in chick_com_item: #남아있는 모든 치킨집
                    #남은 치킨집의 좌표
                    x = chick[c - 1][0]
                    y = chick[c - 1][1]
                    
                    min_dist = min(min_dist, abs(x-i) + abs(y-j))
                ans+=min_dist
            
    ans_list.append(ans)

print(min(ans_list))

