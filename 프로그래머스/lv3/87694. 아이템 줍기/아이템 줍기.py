def chkIn(rc,nx,ny):#사각형 내부에 있는 사각형인지 체크
    ch = True
    for i2,j2,x2,y2 in rc:
        i = 2 * i2
        j = 2 * j2
        x = 2 * x2
        y = 2 * y2
        
        if i<nx<x and j<ny<y:
            ch = False
    return ch
        

def rect(rc): #사각형 좌표 맵핑하기 
    rMap = [[0] * 110 for _ in range(110)]    
    
    for i2,j2,x2,y2 in rc: #사각형의 개수만큼 실행 (최대 4)
        i = 2 * i2
        j = 2 * j2
        x = 2 * x2
        y = 2 * y2
        
        for px in range(x-i+1):
            if chkIn(rc,i+px,j):
                rMap[i+px][j] = 1
        for py in range(y-j+1):
            if chkIn(rc,i,j+py):
                rMap[i][j+py] = 1
        for pi in range(x-i+1):
            if chkIn(rc,x-pi,y):
                rMap[x-pi][y] = 1
        for pj in range(y-j+1):
            if chkIn(rc,x,y-pj):
                rMap[x][y-pj] = 1
            
            
    return rMap

    
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    rMap = rect(rectangle)
    
    q = [[characterX*2,characterY*2]] #시작 좌표 입력
    rMap[characterX*2][characterY*2] = 2
    x = [0,1,0,-1]
    y = [1,0,-1,0]
    while q:
        item =q.pop()
        itx = item[0]
        ity = item[1]
        
        if itx == itemX*2 and ity == itemY*2: #목적지에 도착하면
            print(int(rMap[itx][ity]-2))
            return(int(rMap[itx][ity]-2))
            
        else:        
            for i in range(4): # 0 : 오른쪽 / 1 : 아래 / 2 : 왼쪽 / 3 : 위 _ 동서남북 체크
                nx = itx+x[i]
                ny = ity+y[i]
                if 0 <= nx < len(rMap) and 0 <= ny < len(rMap[0]) and rMap[nx][ny] == 1: #방문가능한 위치라면
                    rMap[nx][ny] = rMap[itx][ity]+0.5
                    #rMap[nx][ny] = rMap[itx][ity]
                    q.insert(0,[nx,ny])

    #for item in rMap:
    #    print(item)
