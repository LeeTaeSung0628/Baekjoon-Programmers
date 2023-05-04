

def solution(N, number):
    
    #한개썼을때 numL[0]
    numL = [] #0번째에는 N이 한개일때의 값을 추가
    numL.append([N])
    if N == number: #정답탐색
        return 1
    
    #두개썼을때 numL[1]
    res = []
    res.append(int(str(N)*2))
    res.append(N+N)
    res.append(N-N)
    res.append(N*N)
    res.append(N//N)
    res = list(set(res)) #중복제거
    for r in res: #정답탐색
        if r == number:
            return 2
    numL.append(res)

    
    #3~8개썼을때 numL[2~8]
    for i in range(2,8):
        res = []
        
        res.append(int(str(N)*(i+1))) #현재 수만큼 N추가
        
        for j in range(1,(i+1//2)+1): #N을 i+1개만큼 사용한 모든경우
            k = i+1 - j
            for numx in numL[j-1]:
                for numy in numL[k-1]:
                    res.append(numx+numy)
                    res.append(numx-numy)
                    res.append(numy-numx)
                    res.append(numx*numy)
                    if numx != 0 and numy != 0:
                        res.append(numx//numy)
                        res.append(numy//numx)
        
        res = list(set(res)) #중복제거
        for r in res:
            if r == number:
                return i+1
            
        numL.append(res)
    
    return -1