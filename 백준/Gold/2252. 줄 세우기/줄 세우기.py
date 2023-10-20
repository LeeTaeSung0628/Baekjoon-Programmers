from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]

"""
위상정렬을 사용하여 구현한다.
위상정렬은 사이클이 없어야하며, 방향이 있는 그래프일때, 순차적으로 어떻게 실행되어야하는지
알고싶을 떄 사용된다.

1. 진입차수와 자신이 갈수있는 노드를 저장하는 배열 2개를 만든다
2. 진입차수가 0인 모든 노드를 큐에 넣는다.
3. 큐에서 하나씩꺼내면서 해당 노드의 간선을 제외하고, 연결되어있는 다음노드의
    진입차수를 1 감속시킨다.
4. 반복하면 위상정렬이 된다.
"""

#진입차수를 저장
degree = [0] * N
#접근할 수 있는 노드를 저장
graph = [[] for _ in range(N)]

for item in arr:
    st, en = item
    graph[st-1].append(en-1)
    degree[en-1] += 1

#진입 차수 0 삽입
q = deque()

for i in range(len(degree)):
    if degree[i] == 0:
        q.append(i)

answer = []

while q:
    now = q.pop()
    answer.append(now+1)
    for item in graph[now]:
        degree[item] -= 1
        if degree[item] == 0:
            q.append(item)

print(" ".join(map(str,answer)))