def solution(n, left, right):
    
    """
    1
    12 22
    123 223 333
    
    n번째 열인 경우, n+1만큼 n반복 후, 1씩 증가.
    left  7 -> 7 // 4 -> 1나머지 3 -> 1번째 칸의 3쨋줄. 
    1234
    2234
    3334
    4444
    
    """
    
    #시작열
    sl = left // n
    #시작행
    sh = left % n
    
    arr = []
    
    for i in range(right - left + 1):
        #시작행이 시작열보다 작거나 같으면 행+1 삽입
        if sh <= sl:
            arr.append(sl+1)
        else:
            arr.append(sh+1)
        
        sh += 1
        
        #행이 범위를 벗어나면 초기화 후 열 다음칸으로
        if sh >= n:
            sh = 0
            sl += 1
        
    # print(arr)
    return arr