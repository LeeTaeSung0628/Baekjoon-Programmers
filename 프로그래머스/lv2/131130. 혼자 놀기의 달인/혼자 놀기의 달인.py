from itertools import combinations

def solution(cards):
    
    box = []
    #카드 수 배열만큼 상자 만들기
    for i in range(len(cards)):
        box.append(i+1)
    
    box_com = list(combinations(box,2))
    

    maxCnt = 0
    for bc in box_com:
        set1 = []
        set2 = []
        check_card = [False] * len(cards) #방문처리
        for i in range(2):
            b = bc[i]
            b = b-1 #(상자번호)상자마다, 조합의 첫번째 인덱스
            while check_card[b] == False: #다음카드를 고를 수 있을때까지(중복x)
                #세트에 카드 추가
                if i == 0: set1.append(b)
                else: set2.append(b)
                
                check_card[b] = True
                b = cards[b]-1 # -1 해줘서 인덱스 처리
                
        maxCnt = max(maxCnt, (len(set1) * len(set2)))
    
    answer = maxCnt
    return answer