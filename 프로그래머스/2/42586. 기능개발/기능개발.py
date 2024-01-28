from math import ceil
from queue import deque


def solution(progresses, speeds):
    """
    100이 넘어가는 시점까지 걸리는 시간
    7 3 9 4 4 4 10
    """
        
    long_day = 0
    answer = []
    days = deque(ceil((100 - p) / s) for p, s in zip(progresses, speeds))
    while days:
        day = days.popleft()
        if day > long_day:
            answer.append(1)
            long_day = day
        else:
            answer[-1] += 1
    return answer
