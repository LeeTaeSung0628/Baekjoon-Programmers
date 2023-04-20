import collections

def solution(clo):
    Counter = collections.Counter
    t_clo = []
    #의상별 개수 분류
    for i in range(len(clo)):
        t_clo.append(clo[i][1])
    dict = Counter(t_clo)

    sumList = []
    
    for i in dict:
        sumList.append(dict[i]) 

    if len(sumList) == 1:
        return sumList[0]
    
    x = sumList[0]+1
    for i in range(1,len(sumList)):
        x = x * (sumList[i]+1)
    

    
    answer = x-1
    return answer