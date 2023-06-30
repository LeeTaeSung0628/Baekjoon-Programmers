"""
    1. 괄호 먼저 처리
        ')' 닫는 괄호를 만나면 여는괄호가 나올떄까지 스텍에서 pop한다.
    2. pop된 녀석들 중 
        * , / 먼저 순서대로 연산
        연산된 녀석을을 + , - 연산

        
"""

import sys
input = sys.stdin.readline

s = list(input().strip())
s.insert(0,"(")
s.append(")")

stac = []
for item in s: #괄호 처리
    if item == ")": #괄호가 끝나면,

        temp = [] #괄호 안의 연산식 저장
        for _ in range(len(stac)):#여는 괄호가 나올떄까지 pop
            sp = stac.pop()
            if sp == "(":
                break
            else:
                temp.append(sp)
        
        # * , / 먼저 처리 
        gn_stack = [] #곱하기 나누기용 스텍
        while temp: #뒤집어져 있음
            tp = temp.pop()
            if tp == "*" or tp == "/": #최근에 들어간 값과, 다음값을 합쳐서 삽입
                st1 = gn_stack.pop()
                st2 = tp
                st3 = temp.pop()
                st_all = st1+st3+st2 #곱하기/나누기 연산 합친 문자열
                gn_stack.append(st_all)
            else:
                gn_stack.append(tp)

        gn_stack.reverse() #pop연산 순서대로 저장할것 이기때문에 뒤집기
        # + , - 처리 
        pm_stack = [] #곱하기 나누기용 스텍
        while gn_stack:
            gp = gn_stack.pop()
            if gp == "+" or gp == "-": #최근에 들어간 값과, 다음값을 합쳐서 삽입
                st1 = pm_stack.pop()
                st2 = gp
                st3 = gn_stack.pop()
                st_all = st1+st3+st2 #곱하기/나누기 연산 합친 문자열
                pm_stack.append(st_all)
            else:
                pm_stack.append(gp)
        
        stac = stac + pm_stack
      
    else:
        stac.append(item)

print(stac[0])

