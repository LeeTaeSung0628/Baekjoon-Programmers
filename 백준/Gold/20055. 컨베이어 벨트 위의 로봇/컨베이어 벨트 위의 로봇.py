import sys
input = sys.stdin.readline

"""
아이디어 : 1. 밸트 회전(내구성소모는 없다)
            1.1 이때 내리는칸에 로봇이 위치하게 된다면 로봇 삭제
        2. 맨 뒤 인덱스 로봇부터 한칸앞으로 이동(내구도가 1이상이고, 앞에 로봇이 없을때) 내구도 소모
        3. 올리는칸(0번째칸)의 내구도가 1이상이도 로봇 올리기 , 내구도 소모
        4. 내구성이 0인 칸들 체크, 이떄 k개 이상이면 종료
"""

# n = 밸트길이 의 반, k = 내구도가 0인게 K개 이상이면 종료
n, k = map(int,input().split())
shild = list(map(int,input().split())) #각 밸트의 내구성
robo = [0] * n

time = 0
zeroCnt = 0 #내구도가 0인 애들 세기
while zeroCnt < k:
    time += 1 #단계

#밸트 회전
    # 1. 밸트회전
    temp = shild.pop()
    shild.insert(0,temp)
    temp = robo.pop()
    robo.insert(0,temp)
    #내리는칸(n-1)에 로봇이 있으면 로봇 삭제
    robo[n-1] = 0

#로봇 이동
    r_l = len(robo)-1
    for i in range(1,len(robo)):
        #내리는칸(n-1)에 로봇이 있으면 로봇 삭제
        robo[n-1] = 0
        if robo[(r_l-i)] == 1: #해당칸에 로봇이 있다면
            if robo[(r_l-i)+1] == 0 and shild[(r_l-i)+1] > 0: #로봇이 이동할수 있으면
                robo[(r_l-i)] = 0
                robo[(r_l-i)+1] = 1
                shild[(r_l-i)+1] -= 1 #내구성 감소
                if shild[(r_l-i)+1] == 0: #내구도가 0이되면 
                    zeroCnt +=1

#로봇 올리기
    if shild[0] > 0: #내구도가 남아있으면
        robo[0] = 1
        shild[0] -= 1 #내구성 감소
        if shild[0] == 0: #내구도가 0이되면 
            zeroCnt +=1


print(time)