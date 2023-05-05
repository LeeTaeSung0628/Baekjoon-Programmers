def solution(trg):
    
    for i in range(1,len(trg)):
        for j in range(len(trg[i])):
            if j == 0:
                trg[i][j] += trg[i-1][j]  #0번째면 자기자신과 같은 인덱스
            elif j == len(trg[i]) -1: 
                trg[i][j] += trg[i-1][j-1]  #해당 줄의 마지막 인덱스면 하나뻰 인덱스
            else:
                maxv = max(trg[i-1][j-1],trg[i-1][j])
                trg[i][j] += maxv #이전 줄의 자기자신값 또는 +1값중 큰값으로
            
    
    #for i in trg:
    #    print(i)
        
    maxindex = 0
    for item in trg[-1]:
        maxindex = max(maxindex,item)
    
    answer = maxindex
    return answer