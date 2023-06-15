def solution(cap, n, deliv, pick):
    deliv = deliv[::-1] #역순으로 뒤집기 ex) arr[3:0:-1] -> 3번 부터 1번 까지 뒤집기
    pick = pick[::-1]

    answer = 0
    h_deliv = 0
    h_pick = 0

    for i in range(n): #뒤집어져 있기때문에 맨 끝부터 방문
        h_deliv += deliv[i] #배달해야할 박스수(누적)
        h_pick += pick[i] #수거해야할 박스수(누적)

        while h_deliv > 0 or h_pick > 0: #해당 (i번째) 집에 하나라도 남아있으면 빼주고 집으로이동, 음수이거나 0이면 방문 안해도 됨
            #수용가능한반큼 배달하고, 수용가능한만큼 수거한다.
            h_deliv -= cap
            h_pick -= cap
            print(n-i,"번째집, ",h_deliv,"/",h_pick)
            answer += (n - i) * 2 #왕복이므로, 거리에 2곱해주기

    return answer
