
def solution(m, n, pud):
    
    mapl = [[0] * m for _ in range(n)]
    mapl[0][0] = 1
    chk = [[False] * m for _ in range(n)]
    
    if len(pud[0]) > 0:
        for x,y in pud:
            chk[y-1][x-1] = True
    
    for i in range(len(mapl)):
        for j in range(len(mapl[0])):
            #print(i,j)
            if (i != 0 or j != 0) and chk[i][j] == False: #시작점이 아니면서 물웅덩이가 아닐때
                if i-1 < 0: #맨위라인일때
                    mapl[i][j] += mapl[i][j-1]
                elif j-1 < 0: #맨왼쪽라인일때
                    mapl[i][j] += mapl[i-1][j]
                else: #둘다 아닐떄
                    mapl[i][j] += mapl[i-1][j]+mapl[i][j-1]
            #for item in mapl:
            #    print(item)
            
    
    answer = mapl[n-1][m-1]
    return answer%1000000007