"""
 문자열 한개를 선택하여 -1, +1 번째가 같은지 각각 비교, 범위를 벗어나면 아웃
"""

def solution(s):
    
    maxlen = 0
    #문자열 한개씩 선택
    for i in range(len(s)):
        
        # i의 바로 앞 뒤가 i와 같을때(짝수)
        next_l = 1
        next_r = 1
        if i-1 >= 0 and i+1 < len(s):
            if s[i] == s[i-1]: #이전거랑 같을때
                next_l = 2
            elif s[i] == s[i+1]: #다음거랑 같을때
                next_r = 2
            #하나라도 겹치는 수가 있으면
            if next_l == 2 or next_r == 2:
                #범위를 벗어나기 전까지 비교 (짝수)
                while i-next_l >= 0 and i+next_r < len(s):
                    #앞뒤가 같다면
                    if s[i-next_l] == s[i+next_r]:
                        next_l += 1
                        next_r += 1
                    else: break
            print(next_l,next_r)
            maxlen = max(maxlen,(next_l-1) + (next_r-1) + 1)
            
        
        #범위를 벗어나기 전까지 비교 (홀수)
        next_a = 1
        while i-next_a >= 0 and i+next_a < len(s):
            #앞뒤가 같다면
            if s[i-next_a] == s[i+next_a]:
                next_a+=1
            else: break
            
        maxlen = max(maxlen,(next_a-1)*2 +1)
        
        
    answer = maxlen
    return answer

