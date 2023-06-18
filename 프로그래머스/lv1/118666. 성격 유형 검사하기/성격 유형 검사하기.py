def solution(sur, cho):
    
    dic = {}
    
    for i in range(len(sur)):
        print(sur[i][0],sur[i][1],cho[i])
        if cho[i] < 4: #좌측[0]값
            if sur[i][0] in dic:
                dic[sur[i][0]] += 4 -cho[i]
            else: dic[sur[i][0]] = 4 - cho[i]
        elif cho[i] > 4: #우측[1]값
            if sur[i][1] in dic:
                dic[sur[i][1]] += cho[i]- 4
            else: dic[sur[i][1]] = cho[i] - 4
            
    print(dic)
    
    ans = ""
    #1번지표
    if "R" in dic:
        l = dic["R"]
    else: l = 0
    if "T" in dic:
        r = dic["T"]
    else: r = 0
    if l < r : ans+="T"
    else: ans+="R"
    
    #2번지표
    if "C" in dic:
        l = dic["C"]
    else: l = 0
    if "F" in dic:
        r = dic["F"]
    else: r = 0
    if l < r : ans+="F"
    else: ans+="C"
    
    #3번지표
    if "J" in dic:
        l = dic["J"]
    else: l = 0
    if "M" in dic:
        r = dic["M"]
    else: r = 0
    if l < r : ans+="M"
    else: ans+="J"
    
    #4번지표
    if "A" in dic:
        l = dic["A"]
    else: l = 0
    if "N" in dic:
        r = dic["N"]
    else: r = 0
    if l < r : ans+="N"
    else: ans+="A"
    
    return ans