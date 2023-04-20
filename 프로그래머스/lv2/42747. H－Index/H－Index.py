def solution(c):
    
    c.sort()
    
    maxv = 0
    count = 0
    
    dic = {}
    
    for i in range(len(c)):
        for j in range(len(c)):
            if c[i] <= c[j]:
                count+=1
        dic[c[i]] = count
        count = 0
    
    print(dic)
    for item in dic:
        if item >= dic[item]:
            maxv = max(maxv,dic[item])
    
    print(maxv)
    return maxv