def solution(s):
    
    cntZero = 0
    cntChange = 0
    
    baseNum = 0
    exs = s
    while True:
        cntChange += 1
        
        x = 0
        #1. 0제거
        for item in exs:
            if item == "1":
                x += 1
            else:
                baseNum += 1 #매번 제거한 0 의 개수
                cntZero += 1 #누적 제거한 0 의 개수
    
        # print(exs)
        #초기화
        exs = str(bin(x))[2:]
        baseNum = 0
        
        #정지 조건
        if exs == "1":
            break
        
    answer = [cntChange, cntZero]
    return answer