def solution(seq, k):
    res = []
    
    start = 0
    end = 0
    if seq[start] == k:#맨처음값 처리
        res.append([end - start,[start,end]]) #좌표가 한칸일때

    end+=1 #끝값 하나 증가
    total = seq[start] + seq[end]
    while end < len(seq):
        
        if total  == k: #현재 상태가 정답이랑 같다면 추가해주고, 스타트/앤드지점 다음칸으로 바꾸기
            res.append([end-start,[start,end]])

            if end+1 < len(seq):
                end+=1
                total += seq[end]
                
                total -= seq[start]
                start+=1
                
            else:
                break
        else:
            if total < k: #작으면 앤드값 늘리기 (맨끝값이 아닐때)
                if end+1 < len(seq):
                    end+=1
                    total += seq[end]
                else:
                    break
            elif total > k: #크면 스타트를 늘리기
                if start >= end and end+1 < len(seq): #스타트지점이 따라잡아버리면
                    end+=1
                    start = end
                    total = seq[end]
                else:
                    total -= seq[start] #이전 스타트값 삭제
                    start+=1
        
    
    res = sorted(res, key = lambda x: (x[0],x[1][0]))
    print(res[0][1])

    return res[0][1]