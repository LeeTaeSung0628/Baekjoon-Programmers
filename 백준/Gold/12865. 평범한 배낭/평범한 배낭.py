"""
    1. 1부터 최대 무게까지 칸을 할당한다
    2. 자신의 무게와, 모든물건을 탐색하며 누적합을 넣는다
        이떄, dp배열을 반대로 탐색(자기자신이 중복될수 있기때문.)
"""
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

dp = [-1] * (m+1) # 무게

for item in maps: #maps에 들어있는 물건들 하나씩 dp에 넣기
    for j in range(m+1): #가장큰 무게부터 탐색
        if dp[m-j] != -1: #값이 존재할때,
            if (m-j) + item[0] <= m: #물건을 넣을 수 있다면
                #추가된 무게 = 추가된무게의 원래값 / 기존값+아이탬가치 
                dp[(m-j) + item[0]] = max(dp[(m-j) + item[0]], dp[m-j]+item[1])
            
    #합치는경우가 아닌 물건 하나만 넣었을때
    if item[0] <= m:
        dp[item[0]] = max(dp[item[0]],item[1])

if max(dp) == -1:
    print(0)
else: print(max(dp))
