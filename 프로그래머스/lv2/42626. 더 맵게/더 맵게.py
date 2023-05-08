from heapq import heappush, heappop

def solution(scov, K):
    
    q = []
    for item in scov:
        #if item < K:
        heappush(q,item)

    cnt=0
    while q[0] < K:
        if len(q) == 1:
            return -1

            
        if len(q) >= 2: 
            x = heappop(q)
            y = heappop(q)
            heappush(q,x + (y * 2)) 
            cnt+=1

            
    return cnt