import itertools

def solution(numbers, target):
    
    res = []
    res2 = []

    res.append(numbers[0])
    res.append(-numbers[0])
    
    for i in range(1,len(numbers)):
        n = len(res)
        res2 = res
        res = []
        for j in range(n):
            res.append(res2[j]+numbers[i])
            res.append(res2[j]-numbers[i])
        
    sum = 0
    for item in res:
        if item == target:
            sum+=1

    answer = sum
    return answer