

def solution(order):
    
    sub = []
    main = []
    answer = 0
    
    #메인컨테이너 초기화
    for i in range(len(order)):
        main.append(i)
    #main = 0,1,2,3,4
    
    #메인의 현재상자 될 수
    mIndex = 0
    
    #하나씩 체크
    for item in order:
        now = item - 1
        # print("지금!", now)
        
        #서브가 비었을때
        if len(sub) == 0:
            #메인 상자가 now보다 크다면 멈춤
            if mIndex > now:
                break
            #메인에 있고, 메인을 넣을 수 있을때
            elif mIndex == now:
                mIndex += 1
                answer += 1
            else:
                #메인 상자를 넣을 수 있을때까지 서브에 저장
                sub = main[mIndex:mIndex+(now-mIndex)]
                #메인 상자 삭제
                mIndex += now-mIndex+1
                answer += 1
            
        else: 
            #서브에 상자가 있고, 서브를 넣을 수 있을때
            if sub[-1] == now:
                sub.pop()
                answer += 1
            #메인에 있고, 메인을 넣을 수 있을때
            elif mIndex == now:
                mIndex += 1
                answer += 1
            #둘다 못넣는다면
            else:
                #메인 상자가 now보다 크다면 멈춤
                if mIndex > now:
                    break
                #아니라면 넣을 수 있음
                else:
                    sub = sub + main[mIndex:mIndex+(now-mIndex)]
                    mIndex += now-mIndex+1
                    answer += 1

        # print(sub, "S")
        # print(mIndex, "M")
    return answer