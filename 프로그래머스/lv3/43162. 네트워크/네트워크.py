def solution(n, com):
    
    q = []
    res = []
    
    for i in range(n):
        count = 0
        q.insert(0,i) # i : 컴퓨터 1번 부터 모두 체크
        
        while q: 
            x = q.pop()
            if com[x][x] == 1: #자신이 활성이면 (이전에 탐색을 안했으면)
                count+=1
            for j in range(n): #x번 컴퓨터랑 연결되어있는 모든 컴퓨터 찾기
                if com[x][j] == 1: #컴 i가 컴 j랑 연결되어 있으면
                    com[x][j] = 0 #비활성
                    com[j][x] = 0
                    q.insert(0,j)
        
        if count != 0:
            res.append(count)

    answer = len(res)
    return answer