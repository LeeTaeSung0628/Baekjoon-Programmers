import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
maps = [list(input().strip()) for _ in range(N)]

# 1. 완벽한 채스판 배열 2개 생성
# 검정 0 / 흰색 1
mapB = []
mapW = []

wb = ["W","B"]
bw = ["B","W"]
for i in range(N):
    tempB,tempW = [],[]
    for j in range(M):
        tempB.append(bw[(j+i) % 2])
        tempW.append(wb[(j+i) % 2])
    mapB.append(tempB)
    mapW.append(tempW)

# 2. 현재 체스판을 기준으로 다시 칠해줘야하는 애들 체크
# sum(누적합배열) 에 맨왼쪽 맨위는 0으로 한칸씩 채워준다
sumB = [[0] * (M+1)]
sumW = [[0] * (M+1)]
for i in range(N):
    tempB,tempW = [0],[0]
    for j in range(M):

        #고칠체스판(maps)와 완벽한체스판B(mapB)를 비교
        if maps[i][j] == mapB[i][j]:
            #같으면 안고쳐도 되니까
            tempB.append(0)
        else:
            #다르면 한번칠하는 1삽입
            tempB.append(1)

        #화이트 버전
        if maps[i][j] == mapW[i][j]:
            tempW.append(0)
        else:
            tempW.append(1)

    sumB.append(tempB)
    sumW.append(tempW)


# 3. 가로 -> 세로 누적합
#가로
for i in range(N+1):
    for j in range(M):
        sumB[i][j+1] += sumB[i][j]
        sumW[i][j+1] += sumW[i][j]
#세로
for i in range(N):
    for j in range(M+1):
        sumB[i+1][j] += sumB[i][j]
        sumW[i+1][j] += sumW[i][j]


# 4. K크기만큼만 포함하는 구간합 맵 만들기
# 위 and 왼쪽이 K-1개 보다 같거나 많아야 가능하다
inf = float("inf")
guganB = [[inf] * (M+1) for _ in range(N+1)]
guganW = [[inf] * (M+1) for _ in range(N+1)]
for i in range(K,N+1):
    for j in range(K,M+1):
        #K*K개 만큼만 구간합을 구하려면
        # 구간합 = 현재칸 - ((위로K칸 + 왼쪽K칸) - (대각선K칸))
        guganB[i][j] = sumB[i][j] - ((sumB[i-K][j] + sumB[i][j-K]) - sumB[i-K][j-K])
        guganW[i][j] = sumW[i][j] - ((sumW[i-K][j] + sumW[i][j-K]) - sumW[i-K][j-K])


# 5. 최소값구하기
minB, minW = inf,inf
for i in range(K,N+1):
    for j in range(K,M+1):
        minB = min(minB,guganB[i][j])
        minW = min(minW,guganW[i][j])

print(min(minB,minW))