import itertools
import copy
import heapq

def solution(k, n, reqs):
    
    """
    1. 완전 탐색을 이용하여, 삼담원의 모든 유형을 구한다
    2. 우선순위큐를 사용해서 유형마다 참가자를 뽑아 기다린 시간을 구한다.
    
    상담 유형 개수 K
    멘토 수 n
    이떄, 맨토는 k중 하나를 갖고, 무조건 k를 한개 포함하여야 한다.
    """    

    #멘토 수에서 상담유형 개수를 뺀만큼의 개수로 삼담유형을 중복있는 조합으로 뽑는다.
    def comcom(case,m,temp,deps):
        temp = copy.deepcopy(temp)

        if len(temp) >= m:
            #모든 조합을 구했으면 mento에 더해서 다시 저장해준다.
            mentoc = copy.deepcopy(mento)
            for item in temp:
                mentoc[item-1] += 1
                
            res.append(mentoc)
            return

        for item in case: #조합을 구하려면, 자기자신보다 크거나 같은것만 뽑아야 한다.
            if item >= deps:
                temp.append(item)
                comcom(case,m,temp,deps)
                temp.pop()
                deps+=1 # 첫번쨰 거를 다 돌렸으면 다시 안돌게

    #모든 상담 유형을 만든다.
    case = []
    #상담유형별 멘토 인원(초기는 1)
    mento = [1] * k

    for i in range(k):
        case.append(i+1)
        
    res = [] 
    temp = []
    comcom(case,n-k,temp,1)
    
    
    answer = 10000001 #기다린 시간을 저장한다
    
    while res:
        now = res.pop()
        
#        1.
#         유형별로 우선순위큐에 담는다.
        qs = [[] for _ in range(k)]
        
        for item in reqs:
            heapq.heappush(qs[item[2]-1], [item[0],item[1]]) #시작시간이 작은 순부터 삽입
        # print(qs)
        temp = 0 #각 케이스별 대기시간 
        
        #상담 유형별로 따로 처리
        for i in range(k):
            
            cnt = now[i] # 현재 유형의 상담원 명수
            end_times = []
            while qs[i]:
                #가장먼저 기다린사람이 나온다.
                now_sd = heapq.heappop(qs[i])        
                start = now_sd[0]
                end = now_sd[1]
                #상담원이 남았다면 상담원 수를 -1 한다.
                if cnt > 0:
                    cnt -= 1
                    heapq.heappush(end_times, start+end)#끝나는시간(시작시간 + 진행시간)을 큐에 저장한다.
                    # print("상담원 남아있당",end_times)
                else: #상담원이 남지 않았다면
                    #큐에서 젤빨리 끝나는 시간을 하나 꺼낸다.
                    first_time = heapq.heappop(end_times)
                    # print("현재 젤 빨리 끝 :",first_time," 시작할애:",start," 상담중인애 :",end_times)
                #     #시작시간이 젤빨리 끝나는 시간보다 더 느리다면
                    if start >= first_time:
                #         #끝나는 시간을 다시 큐에 저장하고 진행한다.
                        heapq.heappush(end_times, start+end)
                #     #시작시간이 잴빨리 끝나는 시간보다 더 빠르다면
                    else:
                        heapq.heappush(end_times, first_time+end) #끝나는 시가간을 큐에 저장하고
                #         #기다린 시간(젤빨리 끝나는시간 - 상담시작시간)을 더해준다.
                        temp += first_time - start
                        # print(first_time - start,"분 추가")
            
        answer = min(answer,temp)
        
    if answer == 10000001: #한번도 초기화 안됬다면 기다린시간 0
        return 0
    return answer