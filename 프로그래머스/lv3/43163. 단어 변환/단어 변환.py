""" 
    1. 하나의 알파벳만 바뀌는 배열을 찾는다.
        - 1.1 현재값을 기준으로 하나반바뀌는값을 q에 인서트 한다
        - 1.2 팝 하고 그값과 비교해 하나의 알파벳만 바뀌는 배열을 찾는다
    2. 해당 배열을 방문할때는 다시 방문 못하도록한다. ( 이유 : 한 번 방문한 배열은 다시방문해도 이전으로 돌아가 무한반복이기 때문)
    
    3. 최단거리를 찾는것 이기 때문에 BFS를 사용
""" 
import copy

def solution(begin, target, words):
    
    q = []
    valList = [0] * (len(words) + 1) #각 문자열별 값 저장 리스트 / begin값 까지 1추가

    #워드 문자열을 각각 리스트로 저장 / 맨앞엔 begin저장
    wList = []
    words.insert(0,begin)
    print(words)
    for w in words:
        wList.append(list(w))
    copywList = copy.deepcopy(wList)# 문자열 위치찾기용

    #하나의 알파벳만 바뀌는 배열을 찾는다.
    q.insert(0,list(begin))
    wList[0] = "0"
    while q:
        item = q.pop() #해당문자열의 배열
        
        if "".join(item) == target: #타겟을 찾으면
            return valList[copywList.index(item)]
        
        for i in range(len(wList)):
            if wList[i] == "0": #못찾게하기
                continue
            cnt = 0 #비교한 문자열마다 몇개의 문자열이 같은지 체크
            for j in range(len(wList[i])):
                if wList[i][j] == item[j]:
                    cnt+=1
                
            #한문자만 다를경우
            if cnt == len(wList[i])-1:
                q.insert(0,wList[i])
                valList[i] = valList[copywList.index(item)] + 1 #추가된문자열의 값은 현재값 + 1
                wList[i] = "0" #못찾게하기
    return 0