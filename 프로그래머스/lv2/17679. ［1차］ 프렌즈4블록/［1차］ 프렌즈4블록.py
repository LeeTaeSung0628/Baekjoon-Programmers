"""
 각 모든 블록에 대해서 우측,아래,대각선을 탐색해서 모두 같은 알파벳이면 체크해준다.
 서치를 모두 마친 후, 체크해준 블록을 삭제한다.
 
 빈칸이 있다면 윗값과 바꿔준다. (반복) 변경할게 없을때 까지.
"""
#해당좌표가 박스에 포함되는지 체크
def check4x4(i,j,ch_map,m,n):
    if i+1 < m and j+1 < n: #벽을 넘지 않을때
        if ch_map[i][j] == ch_map[i][j+1] == ch_map[i+1][j] ==ch_map[i+1][j+1]:
            return True
        else:
            return False
    

def solution(m, n, board):
    

    #반복 사용 맵
    ch_map = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):     
            ch_map[i][j] = board[i][j]
    
    check_Find = True #삭제할 녀석이 더이상 없다면 멈추기
    
    while check_Find:
        
        check_Find = False
        
        remove_arr = []
        #삭제할 녀석들 찾기
        for i in range(m):
            for j in range(n):
                if ch_map[i][j] != 1:
                    if check4x4(i,j,ch_map,m,n):
                        check_Find = True
                        remove_arr.append([i,j])
                        remove_arr.append([i+1,j])
                        remove_arr.append([i,j+1])
                        remove_arr.append([i+1,j+1])
                    
        #삭제하면서지워진 블록 세기
        for item in remove_arr:
            i, j = item
            ch_map[i][j] = 1

        #지워진 부분 채우기(윗값이랑 바꾸기)
        chek_remove = True
        while chek_remove:
            chek_remove = False
            for i in range(1,m):
                for j in range(n):
                    if ch_map[i][j] == 1 and ch_map[i-1][j] != 1 :
                        ch_map[i][j],ch_map[i-1][j] = ch_map[i-1][j],ch_map[i][j]
                        chek_remove = True #하나라도 바꿀게 있다면 반복
                        
        # for c_m in ch_map:
        #     print(c_m)
        
        
    #빈칸 세기
    total = 0
    
    for i in range(m):
        for j in range(n):
            if ch_map[i][j] == 1:
                total += 1 
    answer = total
    return answer