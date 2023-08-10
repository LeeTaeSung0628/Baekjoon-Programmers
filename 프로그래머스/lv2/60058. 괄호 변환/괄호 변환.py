
#올바른 괄호인지 체크
def isPepect(s):
    stack = []
    for item in s:
        if item == "(":
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            
            if stack.pop() == ")":
                return False
    return True
                
def perpectGual(p):
    
  # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if p == "":
        return p
    
  # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    leftG = 0
    rightG = 0
    index = 0
    for i in range(len(p)):
        #괄호추가
        if p[i] == "(":
            leftG += 1
        else: rightG += 1
        #괄호의 개수가 둘다 1 이상이면서 같아지면
        if 0 < leftG and 0 < rightG and leftG == rightG:
            index = i
            break
    
    U, V = p[:index+1],p[index+1:]
    if isPepect(U):
        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        #  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        return U + perpectGual(V)
    else:
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
        #  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        #  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        #  4-3. ')'를 다시 붙입니다. 
        V =  "(" + perpectGual(V) + ")"
        #  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        temp = ""
        for i in range(1,len(U)-1):
            if U[i] == "(": temp += ")"
            else: temp += "(" 
        U = temp
        #  4-5. 생성된 문자열을 반환합니다.
        return V + U
    
    
    
def solution(p):

    answer = perpectGual(p)
    return answer

    