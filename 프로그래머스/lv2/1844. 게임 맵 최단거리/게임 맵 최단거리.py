
def solution(maps):
    res = [] #성공값
    
    x = [0,1,0,-1]
    y = [1,0,-1,0]
    
    q = []
    q.append([0,0]) #출발위치
    maps[0][0] = 2
    count = 2

    while q:

        me = q.pop() #maps[세로][가로]
        count = maps[me[0]][me[1]]+1

        #오른쪽, 아래 우선
        for move in range(4):#1 오른쪽, 2 아래, 3 왼쪽 ,위
            nx = me[0] + x[move]#세로
            ny = me[1] + y[move]#가로
            if len(maps) > nx >= 0 and len(maps[0]) > ny >= 0: #범위를 벗어나지 않으면
                if maps[nx][ny] == 1:#벽이 아니면
                    q.insert(0,[nx,ny])
                    maps[nx][ny] = count #자기위치 check

        if me[0] == len(maps)-1 and me[1] == len(maps[0])-1: #도착시
            return maps[me[0]][me[1]]-1


    return -1
    