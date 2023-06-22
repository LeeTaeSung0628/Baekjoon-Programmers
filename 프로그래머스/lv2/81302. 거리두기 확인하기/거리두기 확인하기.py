"""
    아이디어: 각 인원(P)마다 갈수 있는 모든경로로(O) 2만큼 이동하며 P가 있는지 체크
            한명이라고 다른인원을 만난다면 0리턴
"""
def findP(arr):
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            ch_map = [[0]*5 for _ in range(5)] #재방문 못하게 체크용
            if arr[x][y] == "P": #사람이 있으면 그사람에 대해서 동서남북 2칸씩 모두 방문
                px = [0,1,0,-1]
                py = [1,0,-1,0]
                ch_map[x][y] = 1 #내위치 방문처리
                for p in range(4):
                    nx = x+px[p]
                    ny = y+py[p]
                    if 0 <= nx < len(arr): #범위 안이고,
                        if 0 <= ny < len(arr[0]):
                            if arr[nx][ny] == "P": #테이블일때만
                                return 0 # 사람발견 즉시 끝내기
                            elif arr[nx][ny] == "O" and ch_map[nx][ny] == 0:
                                ch_map[nx][ny] = 1 #해당위치 방문처리
                                #한번 더 반복
                                for p in range(4):
                                    nx2 = nx+px[p]
                                    ny2 = ny+py[p]
                                    if 0 <= nx2 < len(arr): #범위 안이고,
                                        if 0 <= ny2 < len(arr[0]):
                                            if arr[nx2][ny2] == "P" and ch_map[nx2][ny2] == 0: #테이블일때만
                                                return 0
    return 1
                    

def solution(places):
    
    answer = []
    for item in places:
        answer.append(findP(item))
    

    return answer