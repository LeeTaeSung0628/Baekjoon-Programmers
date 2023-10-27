def solution(n, k):
    
    #0제거 후 리스트(문자화)
    pr = str(int(change(n, k)))

    #조건에 맞는 정수를 넣는다!
    isso = []
    temp = ""
    for i in range(len(pr)):
        if pr[i] != "0":
            temp = temp + pr[i]
            
        elif pr[i] == "0":
            if temp != "":
                #1거르기
                if temp == "1":
                    temp = ""
                else:
                    isso.append(int(temp))
                    temp = ""
    #마지막에 남아있다면 삽입
    if temp != "" and temp != "1":
        isso.append(int(temp))
    
    #소수 갯수 체크
    answer = 0
    for item in isso:
        if isSosu(item):
            answer += 1
        
    return answer

def change(n, k):
    
    #n을 k진법으로 변환한다
    ans = ""
    
    while n > 1:
        ans = str(n%k) + ans
        n = n // k
    
    ans = str(n) + ans
    
    return ans

def isSosu(n):
    if n == 1 or n == 0:
        return False
    
    if n == 2:
        return True
    
    #소수인지 판변한다 (1과 자기 자신만 나누어 떨어지는지 첵크 )
    for i in range(2,(int(n**0.5)) + 1):
        #나누어 떨어진다면
        if n % i == 0:
            return False
    
    return True