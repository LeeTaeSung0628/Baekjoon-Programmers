"""
아이디어 : 1. 모든항공원을 탐색한다
        2. 현재 항공권을 기준으로 [A, B] B로 출발할수 있는 항공권이 있는지 탐색
        3. 출발할 수 있는 항공권이 있다면 dfs호출.(깊이를 추가해준다)
          3-1. 이때 깊이가 최대깊이(티켓의 길이)가 되면 배열 반환
          3-2. 배열은 티켓을 호출할때마다 res[]에 저장.
        4. 반환된 배열이 2개 이상일 경우에 알파뱃 순으로 정렬해야한다.
          4-1. 첫번째 배열값부터 비교하여 같이 안은 배열값이 나오면 i
                [i][0]~[i][2]까지 또 한글자씩 비교, 같지 않은 값이 나오면
                그 한단어를 스트링값으로 비교
"""
import copy
answer = []
    
def dfs(begin,chk,res,tick,tf_id):
    global answer
    chk_copy = copy.deepcopy(chk)
    res_copy = copy.deepcopy(res)
    chk_copy[tf_id] = True #현재 티켓 방문처리
    
    ansCheck = False #모든티켓을 사용했는지 확인
    for item in chk_copy: 
        if item == False: #하나라도 사용안한게 있다면 True
            ansCheck = True
    
    if ansCheck == False: # 모든티켓을 확인했다면
        res_copy.append(begin[0])
        res_copy.append(begin[1])
        answer.append(res_copy)
        res_copy = []

    else: #추가할게 남았다면
        res_copy.append(begin[0]) #현재 티켓 결과에 추가
        for i in range(len(tick)):
            if chk_copy[i] == False and tick[i][0] == begin[1]: #아직 방문하지 않았고, 출발지가 현재위치면)
                dfs(tick[i],chk_copy,res_copy,tick,i)

def solution(tick):
    global answer
    
    for i in range(len(tick)): 
        if tick[i][0] == "ICN":
            chk = [False] * len(tick) #방문여부 확인
            res = [] #방문한 티켓정보 저장
            dfs(tick[i],chk,res,tick,i)
    
    
    if len(answer) >= 2:
        answer = sorted(answer, key = lambda x : x, reverse=False)
        return answer[0]
    else:
        return answer[0]