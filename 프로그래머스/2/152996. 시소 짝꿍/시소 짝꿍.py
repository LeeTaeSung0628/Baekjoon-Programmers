def solution(weights):
    """
     1. 두명을 고른다. -> 모든 조합은 = 시간초과
     2. 시소짝궁이 가능한지 구별한다.
     3. 카운트한다.
     
     1. 인원별로 3가지몸무게를 저장한다.
     - (100/200/300)
     2. 딕셔너리에 저장되어있는데, 또 저장된다면 cnt를 더해준다.
     3. 해당사이클에서 cnt를 증가시켰다면 중복 증가를 막는다.
    """
    
    from collections import Counter

    answer = 0
    counter = Counter(weights)
    # print(counter)
    for i in range(100, 1001):
        if counter[i] > 0:
            answer += counter[i] * (counter[i] - 1) // 2 # 같은 수끼리
            answer += counter[i] * counter[i * 3 / 2]
            answer += counter[i] * counter[i * 2]
            answer += counter[i] * counter[i * 4 / 3]

    return answer
    
