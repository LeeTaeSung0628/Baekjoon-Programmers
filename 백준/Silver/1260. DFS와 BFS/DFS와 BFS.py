"""
https://www.acmicpc.net/problem/1260

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제입력 
4 5 1
1 2
1 3
1 4
2 4
3 4

예제출력
1 2 4 3
1 2 3 4
"""

import sys
input = sys.stdin.readline

N,M,V = list(map(int,input().split()))
edge = [list(map(int,input().split())) for _ in range(M)]
gmap = [([0] * N) for _ in range(N)]
check = [False] * N

#깊이우선탐색
dfsList = []
def dfs(st):
        dfsList.append(st+1)
        check[st] = True
        for i in range(N):
            if check[i] == False and gmap[st][i] == 1:
                   dfs(i)

bfsList = []
def bfs(st):
    que = []
    que.append(st)
    while que:
        n = que.pop()
        bfsList.append(n)
        for i in range(N):
              if check[i] == False and gmap[n-1][i] == 1:
                    que.insert(0,int(i+1))
                    check[i] = True
        check[n-1] = True

#그래프 맵 그리기
for i in range(M):
        #양방향 그래프 표시
        gmap[edge[i][0]-1][edge[i][1]-1] = 1
        gmap[edge[i][1]-1][edge[i][0]-1] = 1
        

dfs(V-1)
check = [False] * N
bfs(V)

print(*dfsList) # * = 리스트 압축 해제
print(*bfsList)
