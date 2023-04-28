def solution(n, lo, re):
    
    res_l = []
    res_r = []

    for l in range(len(lo)):
        for r in range(len(re)):
            if lo[l] == re[r]:
                res_l.append(lo[l])
                res_r.append(re[r])
    while res_l:
        lo.remove(res_l.pop())
    while res_r:
        re.remove(res_r.pop())
                
    
    
    lo.sort()
    re.sort()
    answer = n-len(lo)
    
    for l in lo:
        for r in re:
            if l-1 == r or l == r or l+1 == r:
                answer+=1
                re[re.index(r)] = -99
                break
    
    
    return answer