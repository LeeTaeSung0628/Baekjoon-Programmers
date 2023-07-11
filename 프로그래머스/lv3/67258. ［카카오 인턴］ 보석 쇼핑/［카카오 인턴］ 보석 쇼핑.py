def solution(gems):
    
    #사이즈 딕셔너리
    s_dic = {}
    for item in gems:
        s_dic[item] = 0
    
    #총 보석개수
    size = len(s_dic)
    #최소 거리 값
    minDist = 100002
    #최소 거리
    ans = []
    #보석을 담을 딕셔너리
    dic = {}
    #모든보석이 모였다면, 한칸 진출
    left = 0
    #보석이 모이지 않았다면, 한칸진출
    right = 0
    
    #처음 보석 삽입
    if gems[right] in dic:
        dic[gems[right]] += 1
    else: dic[gems[right]] = 1
        
    while left <= right:
        
        #모든 보석이 모였는지 체크
        if size == len(dic):
            
            #최소거리 갱신
            if minDist > right - left:
                ans = [left+1,right+1]
                minDist = right - left
            
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0: #개수가 0개가 되면 삭제
                del dic[gems[left]]
                
            left += 1
            
        else: #없는보석이 있다면
            if right+1 < len(gems):
                right += 1
                #보석 삽입
                if gems[right] in dic:
                    dic[gems[right]] += 1
                else: dic[gems[right]] = 1
            else: #오른쪽이 끝쪽에 닿았으면 왼쪽 추가
                dic[gems[left]] -= 1
                if dic[gems[left]] == 0: #개수가 0개가 되면 삭제
                    del dic[gems[left]]
                left += 1 
        
        

    answer = ans
    return answer