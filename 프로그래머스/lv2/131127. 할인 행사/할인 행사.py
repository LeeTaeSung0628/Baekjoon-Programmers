def solution(want, num, disc):
    
    dic = {}
    ansCount = 0
    
    #내가 원하는 품목 개수 딕셔너리로 생성
    for i in range(len(want)):
        dic[want[i]] = num[i]
        
    print(dic)
    
    #첫 10개는 모두 빼주기
    for i in range(10):
        if disc[i] in dic: #딕셔너리안에 해당 KEY가 있다면
            dic[disc[i]] -= 1
            
        #모두찾았는지 체크
        ansCheck = True
        for item in dic:
            if dic[item] > 0: #하나라도 남은 수량이 있으면
                ansCheck = False
        if ansCheck == True:
            ansCount += 1
    
    
    
    #다음부터 한칸씩이동하며 더하고 빼기
    for i in range(0,len(disc)-10):
        if disc[i] in dic: #맨처음값은 다시 더해주기
            dic[disc[i]] += 1 

        if disc[i+10] in dic: #맨처음값은 다시 더해주기
            dic[disc[i+10]] -= 1 
            
        #모두찾았는지 체크
        ansCheck = True
        for item in dic:
            if dic[item] > 0: #하나라도 남은 수량이 있으면
                ansCheck = False
        if ansCheck == True:
            ansCount += 1
        ansCheck = False
            
    answer = ansCount
    return answer