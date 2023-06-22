def solution(board, skill):
    
    # for m in board:
    #     print(m)
    # print("===========")
    
    #데미지 누적시키기
    dem = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]    #데미지 누적배열(맨끝에 0 배열 한칸씩 추가)
    for item in skill:
        t,x1,y1,x2,y2,pm = item
        if t == 1: #공격
            dem[x1][y1] -= pm
            dem[x1][y2+1] += pm
            dem[x2+1][y1] += pm
            dem[x2+1][y2+1] -= pm
        else: #회복
            dem[x1][y1] += pm
            dem[x1][y2+1] -= pm
            dem[x2+1][y1] -= pm
            dem[x2+1][y2+1] += pm
    
    #누적한값 쭊쭊쭊 이어나가기
    #가로누적
    for i in range(len(dem)):
        temp = 0
        for j in range(len(dem)):
            dem[i][j] += temp
            temp = dem[i][j]

    #세로누적
    for j in range(len(dem)):
        temp = 0
        for i in range(len(dem)):
            dem[i][j] += temp
            temp = dem[i][j]
            
    # for m in dem:
    #     print(m)
        
    #부서지지 않은 건물 수 세기
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + dem[i][j] > 0:
                cnt+=1

    answer = cnt
    return answer