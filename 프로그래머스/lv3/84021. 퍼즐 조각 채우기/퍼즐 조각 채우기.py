"""
아이디어 : 1. 테이블에 놓인 모든 퍼즐조각들 마다 각각의 x값증가량 y값 증가량을 담은 배열 생성(좌표는 1개 지정)
         2. 보드위의 빈공간의 대하여 1.번과 같이 증가량 배열을 생성
         3. 퍼즐조각 증가량을 빈공간 증가량과 모든 출발위치에 대해서 하나하나 비교, 
            이때 오른쪽 90도 회전 후, 변경된 값과도 비교한다.
         4. 이때 포함이 된다면 배열의 길이만큼 카운트를 증가시켜준다.
"""
import copy

def dfs_t(i,j,table,chk,tab_list1,f_i,f_j): #방문가능한 모든 좌표 구하기
    
    x = [0,1,0,-1]
    y = [1,0,-1,0]
    
    for n in range(4): #동서남북 체크
        nx = i+x[n]
        ny = j+y[n]
        if 0 <= nx < len(table) and 0 <= ny < len(table[0]): #범위를 벗어났는지 체크
            if chk[nx][ny] == False and table[nx][ny] == 1: #방문 안했느닞 체크
                chk[nx][ny] = True #방문처리
                dfs_t(nx,ny,table,chk,tab_list1,f_i,f_j) #가능한곳 재 탐색
                tab_list1.append([nx-f_i,ny-f_j])

def dfs_b(i,j,table,chk,tab_list1,f_i,f_j): #방문가능한 모든 좌표 구하기
    
    x = [0,1,0,-1]
    y = [1,0,-1,0]
    
    for n in range(4): #동서남북 체크
        nx = i+x[n]
        ny = j+y[n]
        if 0 <= nx < len(table) and 0 <= ny < len(table[0]): #범위를 벗어났는지 체크
            if chk[nx][ny] == False and table[nx][ny] == 0: #방문 안했느닞 체크
                chk[nx][ny] = True #방문처리
                dfs_b(nx,ny,table,chk,tab_list1,f_i,f_j) #가능한곳 재 탐색
                tab_list1.append([nx-f_i,ny-f_j])
                
def dfs_v(i,j,table,chk): #보드의 빈공간끼리 묶기
    
    x = [0,1,0,-1]
    y = [1,0,-1,0]
    
    for n in range(4): #동서남북 체크
        nx = i+x[n]
        ny = j+y[n]
        if 0 <= nx < len(table) and 0 <= ny < len(table[0]): #범위를 벗어났는지 체크
            if chk[nx][ny] == 0 and table[nx][ny] == 0: #방문 안했느닞 체크
                chk[nx][ny] = chk[i][j] #방문처리
                dfs_v(nx,ny,table,chk) #가능한곳 재 탐색
                
def comp(t,bod_list2): #테이블의 도형을 받아, 보드에 들어갈수 있는지 체크
    
    chk = False
    
    for i in range(len(bod_list2)):
        b = bod_list2[i][0]
        b_v = bod_list2[i][1]
        
        if len(t) == len(b): #t, b : 각각의 도형 내부 배열의 길이가 같다면
            t = sorted(t,key = lambda x: (x[0],x[1]))
            b = sorted(b,key = lambda x: (x[0],x[1]))
            or_t = t
            if t == b :  # x = +x / y = +y
                chk = True
                
            for i in range(len(t)):  # x = -y / y = +x
                temp = t[i][0]
                t[i][0] = t[i][1] * -1 
                t[i][1] = temp
            t = sorted(t,key = lambda x: (x[0],x[1]))
            if t == b :
                chk = True
            t = or_t
            
            for i in range(len(t)): # x = -x / y = -y
                t[i][0] = t[i][0] * -1 
                t[i][1] = t[i][1] * -1
            t = sorted(t,key = lambda x: (x[0],x[1]))
            if t == b :
                chk = True
            t = or_t
            
            for i in range(len(t)): # x = +y / y = -x
                temp = t[i][0]
                t[i][0] = t[i][1] 
                t[i][1] = temp * -1
            t = sorted(t,key = lambda x: (x[0],x[1]))
            if t == b :
                chk = True
            t = or_t
            
        if chk == True:
            print(t,"는 보드에 들어갈수 있따")
            #해당 b_v(b와 같은빈공간에 있는 녀석들) bod_list2[i][0] 값 바꾸기
            for r in range(len(bod_list2)):
                r_b_v = bod_list2[r][1]
                if b_v == r_b_v:
                    bod_list2[r][0] = []
                
            return(len(t))
        
    return 0
def solution(board, table):
    
    chk = [[False] * len(table[0]) for _ in range(len(table))]
    b_chk = [[False] * len(table[0]) for _ in range(len(table))]
    v_chk = [[0] * len(table[0]) for _ in range(len(table))]
    
    
    tab_list1 = [] #테이블 도형 요소 각각의 증가량 배열
    tab_list2 = [] #테이블의 한 다각형의 증가량 배열
    
    bod_list1 = [] #보드 도형 요소 각각의 증가량 배열
    bod_list2 = [] #보드 각각 다각형의 증가량 배열
    
    #테이블 맵핑
    for i in range(len(table)): 
        for j in range(len(table)):
            if table[i][j] == 1 and chk[i][j] == False:
                tab_list1.append([0,0]) #자신에 대한 증가량 저장
                chk[i][j] = True #방문처리
                f_i = i
                f_j = j # f_i,f_j 초기값 저장
                dfs_t(i,j,table,chk,tab_list1,f_i,f_j)
                tab_list2.append(tab_list1) #총 증가량 배열에 저장
                tab_list1 = [] #각각의 증가량 초기화
    
    #같은 빈공간 끼리 묶기
    cc = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0 and v_chk[i][j] == 0:
                cc += 1
                v_chk[i][j] = cc #방문처리
                dfs_v(i,j,board,v_chk)

    #보드 맵핑
    for i in range(len(board)):
        for j in range(len(board)):
            b_chk = [[False] * len(table[0]) for _ in range(len(table))]
            if board[i][j] == 0 and b_chk[i][j] == False:
                bod_list1.append([0,0]) #자신에 대한 증가량 저장
                b_chk[i][j] = True #방문처리
                f_i = i
                f_j = j # f_i,f_j 초기값 저장
                dfs_b(i,j,board,b_chk,bod_list1,f_i,f_j)
                bod_list2.append([bod_list1,v_chk[i][j]]) #총 증가량 배열에 저장
                bod_list1 = [] #각각의 증가량 초기화
                
    print("테이블 증가량")
    for t in tab_list2:
        print(t) #테이블의 모든 도형의 증가량
    
    print("보드 증가량")
    for b in bod_list2:
        print(b) #테이블의 모든 도형의 증가량
    
    print("---------------")
    
    conut = 0
    for t in tab_list2: #t : 각각의 도형
        conut+=comp(t,bod_list2)
        
    print("---------------")
    
    for item in v_chk:
        print(item)
        

    return conut