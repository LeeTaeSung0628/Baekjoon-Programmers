ct = 0 #방문 카운트

def dfs(vist,check,n,numb):
    global ct
    if numb >= n:
        return 0

    if vist[numb] == False:
        vist[numb] = True
        ct+=1

    
    for i in range(n): # i = 송전탑 번호
        #모든송전탑을 방문하도록 함
        if check[numb][i] == True:
            check[numb][i] = False
            check[i][numb] = False
            dfs(vist,check,n,i) #i값은 현재 송전탑에서 방문가능한 송전탑
            check[numb][i] = True
            check[i][numb] = True
            
            

def solution(n, wir):
    global ct

    check = [[False] * (n) for _ in range(n)]
    
    #송전탑의 이어짐을 체크
    for i in range(len(wir)):
        check[wir[i][0]-1][wir[i][1]-1] = True
        check[wir[i][1]-1][wir[i][0]-1] = True


    #송전탑 방문 여부 체크
    vist = [False] * (n)

    #송전탑 방문횟수를 담을 배열
    res = []

    #최종 절댓값 저장
    absList = []

    #하나씩 잘라보면서 연결
    for i in range(len(wir)):
        check[wir[i][0]-1][wir[i][1]-1] = False
        check[wir[i][1]-1][wir[i][0]-1] = False
        for j in range(n):#각 송전탑별 방문할수 있는 최대 송전탑
            dfs(vist,check,n,j)
            if ct != 0: #가능하곳에 모두 방문했으면 다른애들은 방문이 0회
                res.append(ct)
            ct = 0 #초기화

        if len(res) > 1:
            print(i,"번째 짤랐을때 각각 방문횟수 : ",res,end="")
            btween = abs(res[0] - res[1])
            absList.append(btween)
            print(" 두개수의 차이 절댓값 : ",btween)
        check[wir[i][0]-1][wir[i][1]-1] = True
        check[wir[i][1]-1][wir[i][0]-1] = True
        #초기화
        vist = [False] * (n)
        res = []

    minv = 999
    for i in absList:
        minv = min(minv,i)
    answer = minv
    return answer