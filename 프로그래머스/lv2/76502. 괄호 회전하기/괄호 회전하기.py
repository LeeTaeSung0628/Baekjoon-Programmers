from collections import deque

def solution(s):
    
    ds = deque(s)
    
    cnt = 0
    #모든 경우의 수 탐색
    for _ in range(len(s)):
        if corectGual(ds):
            cnt +=1
        ds.append(ds.popleft())  
    
    return cnt

def corectGual(s):
    
    stack = []
    for item in s:
        if item == "{" or item == "(" or item == "[":
            stack.append(item)
        else:
            if len(stack) < 1:
                return False
            
            if item == "}":
                if len(stack) < 1:
                    return False
                if stack.pop() != "{":
                    return False
            elif item == ")":
                if stack.pop() != "(":
                    return False
            elif item == "]":
                if stack.pop() != "[":
                    return False
    
    if len(stack) == 0:
        return True
    else:
        return False
            
        
