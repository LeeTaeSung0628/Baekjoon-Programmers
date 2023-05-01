"""
아이디어 : 1. p를 정렬 후, 중간값을 찾는다
         2. 중간값이 lim/2 보다 크다면, 중간값보다 뒤에있는값은 1개밖에 못들어간다.
         3. 중간값이 lim/2 보다 크지 않다면, 뒤에있는 값들을 기준으로 2번을 반복한다.
         4. 중간값보다 큰 경계를 찾았다면 남은 녀석들로 2-3번을 반복한다.
         5. lim값이 40kg(최소값)이 되면 가장 큰 영역부터 가능한 애 1개씩 넣는다.
         6. 모두다 넣었다면 끝!
"""

def solution(p, limit):
    
    cnt = 0
    p = sorted(p ,reverse = False)
    total = 0
    size = len(p) #변경되기 전 사이즈
    st = 0 #시작점
    while cnt < size: #카운트가 배열의 크기와 같아지면 정지한다.
        lim = limit

        lim -= p.pop()
        cnt+=1
 
        if  len(p) > 0 and len(p) > st :
            if p[st] <= lim: #젤큰애가 들어간후 lim값이 현재 최소값 이상이면(들어갈 수 있으면)
                lim -= p[st]
                cnt+=1
                st+=1

        total+=1
    
    answer = total    
    return answer