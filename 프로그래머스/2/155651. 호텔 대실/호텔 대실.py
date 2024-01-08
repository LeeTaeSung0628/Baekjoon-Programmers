from heapq import heappush,heappop

def converter(string):
    """ string타입 시간을 분단위의 int값으로 반환하는 함수"""
    h,m = string.split(":")
    return int(h)*60+int(m)

def solution(book_time):
    heap = [] # 분단위 book_time 시간을 담을 힙
    last_out = [-10] # 해당 방의 마지막 대실 종료 시각. 첫 방만 가지고 -10분으로 초기화
    # 모든 방을 돌며 입실시간을 기준으로 heappush
    for i,o in book_time:
        i,o = converter(i),converter(o)
        heappush(heap,(i,o))

    # heap 원소가 없을 때까지
    while heap:
        now_in,now_out = heappop(heap) 
        # 만약 가장 빠른 방에 들어갈 수 있다면
        if now_in >= last_out[0]+10: # last_out[0] : 가장 빠른 종료 시간.
            heappop(last_out) # 해당 방의 종료시간을 빼고
            heappush(last_out,now_out) # 현재의 종료시간을 heappush
        else:
            heappush(last_out,now_out) # 그렇지 않다면 새로운 원소(방)를 종료시간으로 추가

    return len(last_out)