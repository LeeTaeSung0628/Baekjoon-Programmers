import sys
input = sys.stdin.readline

N = int(input()) #입력받을 스티커리스트 개수
S = [] #단일 스티커리스트 길이
S_List = [] #단일 스티커 리스트

for i in range(N):
    S.append(int(input())) #단일 스티커리스트 길이
    S_List.append([list(map(int,input().split())) for _ in range(2)]) # 단일 스티커 리스트

def botomUp(S_List,maxv):

    for i in range(2,len(maxv[0])):
        maxv[0][i] = max(S_List[0][i-2]+maxv[1][i-1],S_List[0][i-2]+maxv[1][i-2])
        maxv[1][i] = max(S_List[1][i-2]+maxv[0][i-1],S_List[1][i-2]+maxv[0][i-2])

    
    return(print(max(maxv[0][len(maxv[0])-1],maxv[1][len(maxv[0])-1])))

for i in range(N): # 총 스티커리스트 개수
    maxv = [[0] * (S[i]+2) for _ in range(2)] #받은 배열의 길이만큼 생성
    botomUp(S_List[i],maxv)