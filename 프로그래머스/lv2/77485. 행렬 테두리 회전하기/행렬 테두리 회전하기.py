def solution(row, col, queries):
    
    maps = [[0] * col for _ in range(row)]
    ind = 1
    
    #맵 생성
    for i in range(row):
        for j in range(col):
            maps[i][j] = ind
            ind+=1
            
    def clock(x1,y1,x2,y2):
        minv = 99999999
        f_temp = 0
        
        p_temp = maps[x1][y1]
        for i in range(y1,y2):
            f_temp = maps[x1][i+1]
            maps[x1][i+1] = p_temp

            minv = min(minv,p_temp)
            p_temp = f_temp

        for i in range(x1,x2):
            f_temp = maps[i+1][y2]
            maps[i+1][y2] = p_temp

            minv = min(minv,p_temp)
            p_temp = f_temp

        for i in range(y2,y1,-1):
            f_temp = maps[x2][i-1]
            maps[x2][i-1] = p_temp

            minv = min(minv,p_temp)
            p_temp = f_temp

        for i in range(x2,x1,-1):
            f_temp = maps[i-1][y1]
            maps[i-1][y1] = p_temp

            minv = min(minv,p_temp)
            p_temp = f_temp

        return minv



    res = []

    for item in queries:
        x1 = item[0]
        y1 = item[1]
        x2 = item[2]
        y2 = item[3]
        res.append(clock(x1-1,y1-1,x2-1,y2-1))    
    
    return res