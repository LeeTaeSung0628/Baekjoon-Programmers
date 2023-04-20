from collections import Counter

def solution(p, c):
    
    
    pp = Counter(p)
    cc = Counter(c)
    
    xx = pp-cc
    
    for x in xx:
        return(x)
    
    

    
    
