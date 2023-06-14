def solution(tar):
    
    tar = sorted(tar,key = lambda x: (x[0],x[1]))
 
    #시작지점
    st = tar[0][1]
    #개수
    cnt = 1
    for i in range(1,len(tar)):
        
        if tar[i][0] < st:
            if st > tar[i][1]:
                st = tar[i][1]
            continue
        else: #요격하지 못할 미사일이 있다면
            cnt+=1
            st = tar[i][1]
        
        
    answer = cnt
    return answer