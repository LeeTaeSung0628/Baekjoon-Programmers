import sys
input = sys.stdin.readline

testCase = int(input())
city = []
build = []
win_city = []
for i in range(testCase):
    N, K = map(int,input().split())
    city.append(list(map(int,input().split())))
    temp = []
    for _ in range(K):
        temp.append(list(map(int,input().split())))
    build.append(temp)
    win_city.append(int(input()))

"""
계층형으로 자식들을 저장한다..
자식이 나오지 않을때까지(중복없이 자식들의 값을 모두 더한다
"""

def findSon(check_son,i,now,dist):
    #최하단이면 
    if len(son_tree[now]) == 0:
        maxDistarr[now] = dist
        return dist
    else:
        #자식 중 가장 시간이 긴녀석과 값을 재귀호출로 찾아서 저장
        maxdist = 0
        for item in son_tree[now]:
            #자식 처음 방문이면
            if check_son[item] == False:
                check_son[item] = True
                maxdist = max(maxdist, findSon(check_son,i,item,city[i][item]))
            else: #이미 거리를 구했던 건물이면
                maxdist = max(maxdist, maxDistarr[item])

    #현재 값을 부터 최하단 자식까지의 최대값
    maxDistarr[now] = maxdist + dist
    return maxdist + dist


for i in range(testCase):

#1. 각 도시마다 필요한 자식도시 만들기
    #자식을 저장하는 트리
    son_tree = [[] for _ in range(len(city[i]))]
    
    for build_item in build[i]:
        s, p = build_item
        son_tree[p-1].append(s-1) #자식추가

#2. 목표 건물로 부터 모든 자식 건물 찾기
    #자식중 가장 오래걸리는애 재귀호출
    # 재방문 방지, 테스트케이스, 현재위치, 현재 가중치 삽입
    check_son = [False] * len(city[i])
    #출발점 별 최대시간
    maxDistarr = [-1] * len(city[i])
    print(findSon(check_son,i,win_city[i]-1,city[i][win_city[i]-1]))
