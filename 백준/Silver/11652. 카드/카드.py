import sys
input = sys.stdin.readline

N = int(input())
numList = [int(input()) for _ in range(N)]

numList.sort()

saveNum = 0 #현재항목 저장
cnt = 1 #항목당 개수
resList = [] #카드의 정수와 개수 저장
if N > 1:
    for i in range(1,N):
        if(numList[i] == numList[i-1]):
            cnt+=1

        else: #새로운 녀석 출현
            resList.append((numList[i-1],cnt)) #이전까지의 녀석 개수 저장
            cnt = 1 #초기화

        if i == N-1: #마지막 항목일 경우
            resList.append((numList[i],cnt))

    resList.sort(key= lambda x : (-x[1],x[0]))
    print(resList[0][0])
else: #N의 크기가 1일때
    print(numList[0])