def solution(msg):
    
    """
    1. 현재문자가 딕셔너리에 있는지 확인
     1.1 있으면 뒤에문자까지 합쳐서 확인
      1.1.1 없으면 있는데 까지 출력하고, 없는데까지 딕셔너리에 추가
    2. 처리할 문자가 없거나, 현재 처리한 문자가 끝이면 끝!
     
    """
    
    dic = {}
    
    for i in range(26):
        dic[chr(ord("A")+i)] = i+1
    
    nowIndex = 27
    compIndex = 0
    answer = []
    
    i = 0
    while i < len(msg):
        nowStr = msg[i]
        
        #마지막 한문자처리
        if i+1 == len(msg): 
            answer.append(dic[nowStr]) 
            break
            
        #딕셔너리에 있는 가장 긴문자 찾기    
        cnt = 1
        for j in range(i+1,len(msg)):
            if nowStr+msg[j] in dic: #해당문자 + 다음문자가 딕셔너리에 있을때
                nowStr += msg[j]
                cnt += 1
                #마지막 한단어 처리
                if j+1 == len(msg):
                    answer.append(dic[nowStr])
                    # print(nowStr+msg[j])
                    break
            else:
                dic[nowStr+msg[j]] = nowIndex
                nowIndex += 1
                answer.append(dic[nowStr])
                # print(nowStr+msg[j])
                break
            
        i += cnt
    
    
    return answer