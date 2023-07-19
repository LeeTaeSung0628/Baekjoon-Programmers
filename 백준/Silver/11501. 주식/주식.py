
import sys
input = sys.stdin.readline

n = int(input()) #테스트케이스별
maps = []
for _ in range(n):
    m = int(input())
    maps.append(list(map(int,input().split())))


for m in maps:
    maxnum = 0 #최대값 저장
    total = 0
    for i in range(len(m)-1):
        r_num = (m[len(m)-1-i]) #현재값
        next_r_num = (m[len(m)-2-i]) #다음값

        #첫 번째수
        if i == 0:
            if r_num > next_r_num: #다음수보다 내가 크면
                maxnum = r_num
                total += r_num - next_r_num
            else: #같거나 작으면
                maxnum = next_r_num
            continue
        
        #maxnum보다 큰수가 나올때 까지 전부 사기(차액만큼 +)
        if next_r_num < maxnum:
            total += maxnum - next_r_num
        else : #같거나 더 크면
            maxnum = next_r_num
    
    print(total)
