from collections import deque

def solution(cacheSize, cities):
    
    cash = deque()
    answer = 0
    for i in range(len(cities)):
        
        if len(cash) < cacheSize:
            check = False
            for j in range(len(cash)): #캐쉬에 있으면 삭제
                if cash[j] == cities[i].upper():
                    del cash[j]
                    check = True
                    break
                    
            if check:
                answer+=1
                cash.append(cities[i].upper())
                
            else: 
                answer+=5
                cash.append(cities[i].upper())

        else:
            check = False
            for j in range(len(cash)): #캐쉬에 있으면 삭제
                if cash[j] == cities[i].upper():
                    del cash[j]
                    check = True
                    break
            
            if check:
                answer+=1
                cash.append(cities[i].upper())
                
            else: #캐쉬에 없으면
                answer+=5
                if len(cash) > 0:
                    cash.popleft()
                    cash.append(cities[i].upper())

    return answer

"""
순차적으로 캐시사이즈 만큼 순차적으로 값을 치환해준다.
"""