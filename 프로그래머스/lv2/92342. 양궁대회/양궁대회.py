"""
우선순위값 식 : 1. 뺏는경우 : (점수 X 2) / 이용된 화살
             2. 빈칸에 쏘는경우 : 점수
             
    현재 쏠수 있는경우(뻇기 or 빈칸) 중 가장 우선순위가 높은 값 
"""
pomuList = []

def pomu(tf,cnt,exList):
    exList = exList.copy()
    
    if len(exList) == cnt:
        pomuList.append(exList)
        return
    
    for item in tf:
        exList.append(item)
        pomu(tf,cnt,exList)
        exList.pop()
    
def solution(n, info):
    
    tf = [True,False]
    pomu(tf,11,[])
    
    df = [] #점수 차이를 저장할 배열
    for pom in pomuList:
        #라이언/어피치 점수 구하기
        ryan = 0
        apeach = 0
        r_b = 0 #라이언의 화살개수
        r_info = [0] * len(info)
        for i in range(len(info)):
            if pom[i] == True:  #pom[i] 에는 10번부터 T/F
                r_b+=info[i]+1    #사용한 화살개수 (어피치보다 1발 추가)
                r_info[i] = info[i]+1
                ryan+=(10-i) #해당 과녁을 이겼을경우 해당과녁판의 점수
            elif pom[i] == False and info[i] > 0:
                apeach+=(10-i) #어피치 점수
        
        if r_b <= n:  #화살개수가 초과되지 않은경우만
            r_info[10] += (n - r_b) #남은화살 개수만큼 0번 과녁에 쏴버리기
            df.append([ryan-apeach,r_info])
    
    df = sorted(df,key = lambda x : (x[0]),reverse=True)
    maxv = df[0][0]
    
    if maxv <= 0: #이긴 경우가 없으면
        return [-1]
    
    res = [] #공통최대값들의 배열
    
    for item in df:
        if maxv == item[0]:
            res.append(item[1]) # res에 공통최대값 삽입
    
    answer = res[0]
    for r in res: #하나씩 비교
        for i in range(len(r)): 
            if answer[10-i] < r[10-i]: # 0번 과녁 부터 비교
                answer = r
                break
            elif answer[10-i] == r[10-i]:
                continue
            else:
                break
                
        
    return answer