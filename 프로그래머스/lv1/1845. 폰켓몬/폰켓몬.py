def solution(nums):
    chk = [0]
    yn = 1 
    for i in range(len(nums)):
        for j in range(len(chk)):
            if chk[j] == nums[i]:
                yn = 1 #이미 존재함
                break
            else: 
                yn = 0 #한개도 없을때
                
        if yn == 0:      
            chk.append(nums[i])
    
    if len(nums) / 2 < len(chk) -1:
        answer = len(nums)/2
    else:
        answer = len(chk) -1
    return answer