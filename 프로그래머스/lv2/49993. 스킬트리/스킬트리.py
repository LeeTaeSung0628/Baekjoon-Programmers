def solution(skill, skill_trees):
    
    cnt = 0
    #skill에 있는 인덱스가 순서대로 등장했는지 체크한다.
    for item in skill_trees:
        #한 스킬트리씩 체크 한다.
        
        #가능?
        check = True
        
        #마지막문자와 같은것을 발견하면 pop할 스텍
        stack = list(skill)
        stack.reverse()
        for s in item:
            #해당 스킬이 선행스킬이 필요없으면 건너뛰기
            if s not in stack:
                continue
            
            #해당 스킬이 배워야할 선행스킬이면 스텍 Pop
            elif s == stack[-1]:
                stack.pop()
                continue
            
            #배우지 못할 선행스킬이면 불가능
            else:
                check = False
                break
        
        if check:
            cnt += 1 
    
    answer = cnt
    return answer