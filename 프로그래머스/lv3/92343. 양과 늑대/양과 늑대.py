"""
아이디어 : 방문가능한 배열을 저정한다..  배열마다 모든경우의 수를 방문 하는 dfs를 실행시킨다.
        이때, 역행도 가능하므로 따로 자식외에 방문 가능한 배열을 따로 저장해둔다. 
        양의 최대 수를 리턴한 경우의 수가 정답이다.
"""
import copy

resList = []
def dfs(i,arr,ed,info,count,res): # 현재위치 / [[부모],[자식,자식]] / 양늑대 / 카운트
    global resList

    arr = copy.deepcopy(arr)
    
    arr.remove(i) #방문한 위치 지우기
    
    if info[i] == 0:
        count+=1
        res+=1
    elif info[i] == 1 and count-1 > 0:
        count-=1
    else: #더이상 가면 늑대가 많아짐
        return resList.append(res)

    for sonList in ed[i][1]: #방문가능한자식 추가
        arr.append(sonList) #arr에는 내자식과 기존 방문하지 않은 위치가 저장됨
    for k in arr: #자식들 하나씩 방문
        dfs(k,arr,ed,info,count,res)

    if len(arr) <= 0:
        return resList.append(res)

def solution(info, edge):
    global resList

    ed_info = []# 인덱스가 자신의 자식과 부모를 갖는 배열 생성[[부모],[자식,자식]]
    for i in range(len(info)):
        son = []
        for j in range(len(edge)): #자식찾기
            if i == edge[j][0]:
                son.append(edge[j][1])
        
        par = []
        for j in range(len(edge)): #부모찾기
            if i == edge[j][1]:
                par.append(edge[j][0])
        
        ed_info.append([par,son])
        
    count = 0
    dfs(0,[0],ed_info,info,count,0) #현재위치/[앞으로 방문할 위치들]
    
    #print(resList)
    answer = max(resList)
    return answer

