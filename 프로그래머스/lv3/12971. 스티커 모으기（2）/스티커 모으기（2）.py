import copy

def solution(sticker):

    """
    솔루션 : dp를 이용한다. 
            첫번째 스티커부터 시작한다.
            자신을 선택하고 2개 다음꺼를 선택한경우, 그것또한 스킵하고 그다음껄 선택한경우
    """
    if len(sticker) == 1:
        return sticker[0]
    
    d1, d2 = [0] * len(sticker), [0] * len(sticker)
    
    # d1은 맨 앞 뜯는 경우
    d1[0] = sticker[0]
    d1[1] = d1[0]
    for i in range(2, len(sticker)-1):
        d1[i] = max(d1[i-2]+sticker[i], d1[i-1])
    
    # d2는 맨 앞 뜯지 않는 경우
    for i in range(1, len(sticker)):
        d2[i] = max(d2[i-2]+sticker[i], d2[i-1])

    return max(d1[-2], d2[-1])

