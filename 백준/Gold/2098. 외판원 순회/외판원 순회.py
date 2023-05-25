import sys
import heapq
input = sys.stdin.readline

n = int(input())

maps = [list(map(int,input().split())) for _ in range(n)]
INF = float("inf")

#dp[출발지][방문여부(1~16)]
dp = [[-1]*(2**n) for _ in range(n)] #현재를 기준으로 남은 정점을 모두 채우고 원점으로 돌아가는 값

def dfs(now,state):
    
    if state == (2**n)-1: #모든 정점을 다 돌았다면
        if maps[now][0] == 0: #원점으로 돌아갈 수 없다면
            return INF
        else:
            dp[now][state] = maps[now][0]
            return dp[now][state]
        
    if dp[now][state] != -1: #이미 방문한 곳이라면
        return dp[now][state]

    minDist = INF
    for k in range(n):
        if state & (1 << k) == 0 and maps[now][k] != 0: # 아직 방문하지 않았고, 방문 가능한 정점일때
            minDist = min(minDist, dfs(k,state | (1 << k)) + maps[now][k])

    dp[now][state] = minDist
    return minDist

print(dfs(0,0 | (1 << 0)))

