"""
    아이디어 : 진실을 아는사람이 포함된 모든 파티를 찾는다
             그 파티에 포함된 사람도 진실을 아는 모임에 넣는다 
             탐색하지 않은 파티를 탐색하고, 남은 파티가 정답이다.
"""
import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # n : 사람수 / m : 파티 수
t = list(map(int,input().split())) # 진실을 아는 사람
party = [list(map(int,input().split())) for _ in range(m)] # 파티마다 오는 사람

cnt = 0
checkPlus = True
p_ck = [False] * m #방문체크

while checkPlus == True:
    checkPlus = False #반복체크

    for i in range(len(party)): #파티마다 체크
        chk = False #진실을 아는자가 있는지

        for j in range(1,len(party[i])): #파티별 인원 체크
            for k in range(1,len(t)):
                if t[k] == party[i][j]:
                    chk = True
        
        if chk == True and p_ck[i] == False: #해당파티는 진실이 있는 파티임 and 아직 방문 안했으
            for j in range(1,len(party[i])): #파티별 인원 체크
                    t.append(party[i][j])
                    list(set(t))#진실을 아는모임에 추가
                    p_ck[i] = True

                    checkPlus = True #다시 반복
    
for item in p_ck:
     if item == False:
          cnt+=1

print(cnt)