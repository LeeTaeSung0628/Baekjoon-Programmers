
import sys
import heapq
input = sys.stdin.readline

n = int(input()) #정점 개수
e = int(input()) #엣지 개수
edge = [list(map(int,input().split())) for _ in range(e)] #간선
startPoint , endPoint = map(int,input().split())

inf = float("inf")
#맵 만들기
maps = [[inf] * n for _ in range(n)]

for item in edge:
    st, en, dist = item
    if maps[st-1][en-1] > dist:
        maps[st-1][en-1] = dist

q = []
# q = [시작점,누적거리합,누적좌표값]
heapq.heappush(q,[startPoint-1,0,[startPoint-1]])
distArr = [[inf,[]] for _ in range(n)]
while q:
    now, now_dist, total = heapq.heappop(q)
    
    if distArr[now][0] > now_dist:
        distArr[now][0] = now_dist
        distArr[now][1] = total
        for i in range(len(maps[now])):
            next_city = i
            next_dist = maps[now][i]
            if next_dist != inf:
                heapq.heappush(q,[next_city,next_dist + now_dist, total + [next_city]])

print(distArr[endPoint-1][0])
print(len(distArr[endPoint-1][1]))
for i in range(len(distArr[endPoint-1][1])):
    if i == len(distArr[endPoint-1][1])-1: #마지막이면
        print(distArr[endPoint-1][1][i]+1,end="")
    else: print(distArr[endPoint-1][1][i]+1,end=" ")