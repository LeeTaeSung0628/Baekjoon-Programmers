

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

#가장 긴 증가하는 부분수열 찾기
"""
1. 비어있는 이진탐색 배열을 만든다
2. 초기값을 삽입해 준다
3. 이제부터 값을 삽일할 때 마다..
    맨마지막 원소보다 크면 삽입
    크지 않으면 넣고자 하는 값보다 큰 가장 가까운 값과 교체
"""

bin_arr = []
bin_arr.append(arr[0])

#값 추가 하거나, 교체
def LIS(num):
    #마지막 인덱스보다 크면 삽입
    if num > bin_arr[-1]:
        bin_arr.append(num)
        return

    #이진탐색으로 들어갈 자리 찾기
    st = 0
    end = len(bin_arr)-1
    
    mid = (st+end) // 2
    while st < end:
        mid = (st+end) // 2
        if num <= bin_arr[mid]: #작거나 같다면 줄이기(num 이상인 애를 찾기위해)
            end = mid
        elif num > bin_arr[mid]:
            st = mid+1
        elif num == bin_arr[mid]:
            bin_arr[mid] = num
            break
    bin_arr[end] = num

for i in range(1,len(arr)):
    LIS(arr[i])

print(len(bin_arr))


"""
4
1 7 10 2
"""