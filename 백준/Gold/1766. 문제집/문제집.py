
import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())

answer = []
graph = [[] for _ in range(n + 1)]
inDegree = [0 for _ in range(n+1)]
queue = []


for i in range(m):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    graph[first].append(second)
    inDegree[second] += 1

for i in range(1, n + 1):
    if inDegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(queue, i)


print(" ".join(map(str, answer)))
# #실패코드 
# import sys
# import heapq
# input = sys.stdin.readline

# N, M  = map(int, input().split())
# edge = [list(map(int, input().split())) for _ in range(M)]

# """
#  1. 트리 구조의 맵을 만든다
#  2. 현재 트리구조에서 최하단 노드를 재귀호출로 찾는다.
#  3. 찾은 최하단 노드들을 우선순위 큐에 넣어순서대로 처리한다
#  4. 처리한 최하단 노드들은 체크처리 하여 다시 찾지 못하도록한다.

# """
# #트리 구조의 맵을 만든다
# treeP = [[] for _ in range(N)] #부모노드가 루트노드 
# treeC = [[] for _ in range(N)] #자식노드가 루트노드
# for item in edge:
#     st ,en = item
#     treeC[en-1].append(st-1)
#     treeP[st-1].append(en-1)

# #모든 루트노드를 찾는 함수
# def findAllRoot(treeP):
#     par = []
#     for i in range(len(treeP)):
#         if len(treeP[i]) == 0: #길이가 0이면 루트
#             par.append(i)
#     return par

# #자신 트리의 모든 최하단 노드를 찾는 함수
# def findChild(x,treeC,checkTree,visit):

#     if len(treeC[x]) == 0 and checkTree[x] == False: #최하단 노드이면
#         chileList.append(x)
#         checkTree[x] = True #처리한 녀석은 표시한다
#         return
    
#     #자식들의 자식들을 찾아서
#     checkQ = False
#     for c in treeC[x]:
#         if checkTree[c] == False:
#             findChild(c,treeC,checkTree,visit)
#         if visit[c] == False: #큐에서 자식들이 하나라도 처리가 안되었다면
#             checkQ = True
    
#     if checkTree[x] == False and checkQ == False: #자식이 모두 처리됨
#         chileList.append(x)
#         checkTree[x] = True
#         return

# rootList = (findAllRoot(treeP)) #루트 리스트

# #찾은 자식노드를 q에 넣는다
# #모든 루트 노드별로 최하단 노드를 불러낸다
# checkTree = [False] * N #최하단 중복방문 방지
# visit = [False] * N #실제 q에서 사용되었는지
# chileList = []
# #방문하지 않은 최하단 노드 출력
# for x in rootList:
#     findChild(x,treeC,checkTree,visit)

# q  = chileList
# heapq.heapify(q)

# #결과값을 저장
# ans = []
# while q:
#     now = heapq.heappop(q)
#     ans.append(now+1)
#     visit[now] = True 

#     #다시 아직방문하지 않은 최하단 노드를 찾는다
#     chileList = []
#     for x in rootList:
#         findChild(x,treeC,checkTree,visit)
#     for c in chileList:
#         heapq.heappush(q,c)

# print(" ".join(map(str,ans)))

# """
# 4 2
# 1 4
# 3 2
# """