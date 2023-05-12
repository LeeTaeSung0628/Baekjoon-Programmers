"""
    귤 k개를 골랐을때 크기가 각기다른 종류가 최소인 값을 찾거라
    -> 1:2 , 2:1 , 3:3, 4:2
    
    4개 고르려면 2,3 / 1,4
    k보다 작은 귤중 가장 큰녀석부터 담는다.
    //
    정렬을 한 후, 이전과 다른값이 나오면 이전의 값의 개수만큼 더해준다.
"""

def solution(k, tang):
    tang.sort()
    tang.append(-1) # 끝값삽입하여 마지막값 얻기
    
    t_dic = [] # 귤 크기별 개수
    
    chk = tang[0]
    cnt = 1
    for i in range(1,len(tang)):
        if chk == tang[i]:
            cnt+=1
        else:
            t_dic.append([chk,cnt]) #[크기, 개수]
            cnt = 1
            chk = tang[i]
    
    t_dic = sorted(t_dic, key = lambda x: x[1],reverse = True)
    
    resCount = 0
    #k보다 작은 녀석(가능한) 들중, 가장 큰녀석 만큼 빼고 카운트하기

    for t in t_dic: #만약 k보다 귤개수가 더 크거나 같면 다 같은 귤개수로 하면된다.
        if k > t[1]: # ex) k = 5 일대 귤개수는 최대 4개
            k-=t[1]
            resCount+=1
        elif k <= t[1]:
            k-=t[1]
            resCount+=1
            return resCount
    
    answer = 0
    return answer