def solution(bandage, health, attacks):
    
    """
        초당 x만큼 회복.
        해당 초만큼 연속으로 묶는데 성공하면 y만큼 추가 체력.
        
        0에서 시작하여, 다음 공격에 맞기 전까지의 시간 x
        (x * bandage[1]) + ((x // bandage[0]) * bandage[2])
    """
    
    now_hel = health
    now_time = 0
    
    for item in attacks:
        # x : 이전공격에서부터 지난 시간
        x = item[0] - now_time -1
        #시간 증가
        now_time = item[0] 

        #이때까지의 회복
        now_hel += (x * bandage[1]) + ((x // bandage[0]) * bandage[2])
        if now_hel > health: now_hel = health
        
        #공격에 맞은 순간이다.
        now_hel -= item[1]
    
        if now_hel < 1 : return -1
    
    

    return now_hel