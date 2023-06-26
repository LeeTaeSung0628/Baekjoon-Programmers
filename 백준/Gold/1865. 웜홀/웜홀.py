"""
' 방향없는 간선 그래프, 방향이 있는 웜홀이 하나있다. 
  웜홀 : 시작 -> 도착 하나의 경로, 도착하게 될때, 시작했을때 보다 시간이 거꾸로간다 '
  
  밸만 포드 알고리즘 사용

"""
import math
import sys
import heapq
input = sys.stdin.readline

testCase = int(input())
n =[] #정점 개수
m = [] #간선 개수
w = [] #웜홀 개수
edge = []
w_h = []
for _ in range(testCase):
    n_item, m_item, w_item = map(int,input().split())
    n.append(n_item)
    m.append(m_item)
    w.append(w_item)
    #간선입력
    temp = []
    for _ in range(m_item):
        x,y,num = map(int,input().split())
        temp.append([x,y,num]) #양방향 입력
        temp.append([y,x,num])
    #웜홀 입력
    for _ in range(w_item):
        x,y,num = map(int,input().split())
        temp.append([x,y,-1*num]) #시간줄이기
    edge.append(temp)

def b_f(st,num):
    dist_arr[st][st] = 0

    for i in range(n[num]): #내 정점부터 모든 정점에 대해
        for item in edge[num]: #모든 간선에 대해
            x, y , cost = item #x는 y에 cost로 연결되어있으니까,
            x=x-1
            y=y-1
            #if dist_arr[st][x] != INF: #시작점으로 연결되있고,
                #y로 바로가는값보다, x에 가서,y로 가는 비용이 더 싸면? 
            if dist_arr[st][y] > dist_arr[st][x] + cost:
                dist_arr[st][y] = dist_arr[st][x] + cost
                #간선개수(정점개수(n-1) -1)보다 한번더 반복하면 음수싸이클이 있다는 뜼
                if i == n[num]-1:
                    return False
    return True

INF = 2500*2*10000+1
#해당 정점부터 다른정점까지의 방문 거리!
for case in range(testCase):
    dist_arr = [[INF] * n[case] for _ in range(n[case])]
    if (b_f(0,case)): print("NO") #각 정점에 대해서 구할필요는 없음 (이문제에서는!)
    else: print("YES")
    #print(dist_arr)
