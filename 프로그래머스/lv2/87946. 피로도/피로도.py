
res = []
def dfs(g, k, dun,check):

    res.append(g)
    
    for i in range(len(dun)):
        if k >= dun[i][0] and check[i] == False:
            check[i] = True
            dfs(g+1,k-dun[i][1],dun,check)
            check[i] = False
    
def solution(k, dun):
    check = [False] * len(dun)
    dfs(0,k, dun,check)
    
    maxv = 0
    for i in res:
        maxv = max(maxv,i)
    
    answer = maxv
    return answer