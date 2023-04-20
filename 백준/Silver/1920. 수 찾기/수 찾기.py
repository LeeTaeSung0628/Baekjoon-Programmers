import sys
input = sys.stdin.readline

M = int(input())
numList = list(map(int,input().split()))
N = int(input())
targetList = list(map(int,input().split()))


def search(st, en, target):

    if st==en:
        if numList[st] == target:
            return print("1")
        else:
            return print("0")
    
    mid = (st + en) // 2

    if target > numList[mid]:
        search(mid+1, en, target)
    else:
        search(st, mid, target)

numList.sort()

for i in range(N):
    search(0,M-1,targetList[i])