def solution(p_b):
    
    if len(p_b) == 1:
        return True
    
    p_b.sort()
    
    for i in range(1,len(p_b)):
        if p_b[i-1] in p_b[i][0:len(p_b[i-1])]:
            return False
    return True
                