def solution(record):
    
    """
        1. 방안에서 변경시 즉시 변경
        2. 밖에서 변경후 들어왔을때 변경
        
        자료구조 : uid와 모든 행동이 담긴 배열
                 uid별 최신 닉네임 맵         
    """
    
    all_info = []
    dic = {}
    
    for item in record:
        
        isp = item.split()
        
        action = isp[0]
        uid = isp[1]
        #있는경우만!
        if len(isp) > 2:
            name = isp[2]
                   
        if action == "Enter":
            all_info.append([uid,"님이 들어왔습니다."])
            dic[uid] = name
            
        elif action == "Leave":
            all_info.append([uid,"님이 나갔습니다."])
            
        elif action == "Change":
            dic[uid] = name
    
    # print(all_info)
    # print(dic)
    
    answer = []
    
    #삽입
    for item in all_info:
        uid, text = item
        answer.append(dic[uid]+text)
    
    return answer