def solution(idl, rep, k):
    
    dic = {}
    cnt = 0
    for item in idl:
        dic[item] = cnt
        cnt+=1
    
    ss_list = [[] for _ in range(len(idl))]
    for item in rep:
        #ss => 신고자
        #nn => 당한사람
        ss, nn = item.split()
        ss_list[dic[nn]].append(dic[ss])
    
    
    mail_list = [0] * len(idl)
    for item in ss_list:
        item = list(set(item)) # 중복제거
        if len(item) >= k:
            for i in item:
                mail_list[i] += 1

        
    answer = mail_list
    return answer