from itertools import combinations
from itertools import permutations
import sys
input = sys.stdin.readline

n  = int(input())

rdd_list = [] #함수리스트
arr_list = [] #배열리스트

for _ in range(n):
    rdd_list.append(input().strip())
    _ = input()
    arr_list.append(input().strip())



#arr_list 정수형으로 사용하기
n_list = []
for item in arr_list:
    if len(item) > 2:
        arr_part = list(map(int,item[1:len(item)-1].split(",")))
        n_list.append(arr_part)
    else:
        n_list.append([])

#RD , LD 개수 및 R이 홀수인지 짝수인지 알아내기
total_RD = []
state = 0 #0이면 정방향(이때삭제하면 LD) 1이면 리버스
for item in rdd_list:
    l_temp = 0
    r_temp = 0
    state = 0 #초기화
    for i in range(len(item)):
        if item[i] == "R":
            if state == 0: state = 1
            else: state = 0
        
        if item[i] == "D":
            if state == 0: l_temp+=1
            else: r_temp+=1
    total_RD.append((l_temp,r_temp,state))

for i in range(len(n_list)):
    l = len(n_list[i])
    LD = total_RD[i][0]
    RD = total_RD[i][1]
    st = total_RD[i][2]

    if l - (LD + RD) < 0: #배열길이보다 더많이 삭제하면
        print("error")
        continue

    #ld,rd만큼 삭제하고, 상태에 따라 출력
    if st == 0:
        ans = n_list[i][LD:l-RD]
        print("[",end="")
        for ch in range(len(ans)):
            print(ans[ch],end="")
            if ch < len(ans)-1:
                print(",",end="")
        print("]")
    else:
        ans = n_list[i][LD:l-RD]
        print("[",end="")
        for ch in range(len(ans)-1,-1,-1):
            print(ans[ch],end="")
            if ch > 0:
                print(",",end="")
        print("]")