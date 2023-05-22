
import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

arr = [0] * (n + 1) # 0부터 n-1까지의 수를 저장할 어레이

#=====---====---====----===-----

def prefix_sum(i): # i번까지의 누적합
    res = 0
    while i > 0: #0이 될때까지 반복
        res += tree[i]
        #0이 아닌 마지막 비트만큼 빼면서 이동
        i -= (i & -i)

    return res

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

def update(x, y):
    while x <= n: #자신을 포함하여 누적합을 더한애들꺼 전부 더해주기
        tree[x]+=y
        x += (x & -x)

#값 삽입
for i in range(1, n + 1):
    x = int(input())
    arr[i] = x


tree = [0] * (n + 1) # 바이너리 인덱스 트리
sum_arr = [0] * (n + 1) #누적합
#트리에 값 넣기
temp = 0
for i in range(1,len(arr)):
    temp+=arr[i]
    sum_arr[i] = temp
    tree[i] = sum_arr[i] - sum_arr[i - (i & -i)] #갖고 있는 비트수 만큼 이전까지 더해서 갖는다..비트수가 1이면 자기자신만 갖음



for i in range(m + k):
    a, b ,c = map(int, input().split())

    #업데이트 연산
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c

    #구간합 연산
    else:
        print(interval_sum(b, c))