import sys

input = sys.stdin.readline

k = int(input())
hasugu = list(map(int,input().split()))


"""
1. 하수구 위치가 가운데 위치하는지 찾는다
    가운데 위치하면 4개위 위치를 채우고 하수구 위치를 채운 나머지 위치를 마저 채운다
2. 가운데 위치하지 않는다면 위치한 칸을 기준으로 해당구역을 모두 칠한다
     - 모두칠할때 x, y에 대해서 (2^k / 2) -1 이하이면 x,y가 모두 이하인 칸을 다 칠한다
     그후 나머지 4개 꼭지점 위치를 다 칠해주고
     나머지 위치를 마저 채운다
"""

if k == 1:
    hasugu = [hasugu[1]-1, hasugu[0]-1]
    hasugu = [ 1 - hasugu[0], hasugu[1]]
    #색칠할 맵 생성
    maps = [[0] * 2 for _ in range(2)]
    #꼭지점 생성
    ggog = [[0,0],[0,int(2**k)-1],[int(2**k)-1,0],[int(2**k)-1,int(2**k)-1]]
    #중간값
    mid = (int((2**k / 2)  -1))
    #색칠 카운트
    color = 0

    maps[hasugu[0]][hasugu[1]] = -1

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 0:
                maps[i][j] = 1
else:
    hasugu = [hasugu[1]-1, hasugu[0]-1]
    hasugu = [ 3 - hasugu[0], hasugu[1]]
    #색칠할 맵 생성
    maps = [[0] * int(k**2) for _ in range(int(k**2))]
    #꼭지점 생성
    ggog = [[0,0],[0,int(2**k)-1],[int(2**k)-1,0],[int(2**k)-1,int(2**k)-1]]
    #중간값
    mid = (int((2**k / 2)  -1))
    #색칠 카운트
    color = 0

    #하수구 중간인지 찾기
    if  mid <= hasugu[0] < int(2**k -1) and mid <= hasugu[1] < int(2**k -1):
        nx = [0,1,0,-1]
        ny = [1,0,-1,0]

        #꼭지점 별로 채우기
        for item in ggog:
            color += 1
            maps[item[0]][item[1]] = color
            for i in range(4):
                px = item[0] + nx[i]
                py = item[1] + ny[i]
                if 0 <= px < int(2**k) and 0 <= py < int(2**k):
                    maps[px][py] = color

        #나머지 빈칸 채우기
        color += 1
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == 0:
                    maps[i][j] = color

        #하수구 채우기
        maps[hasugu[0]][hasugu[1]] = -1

    #중간이 아니다    
    else:
        #하수구가 4사분면중 어디있는지 찾기
        if hasugu[0] <= mid and hasugu[1] <= mid: #왼쪽 위
            #하수구있는 사분면 채우기
            color += 1
            for i in range(0,mid+1):
                for j in range(0,mid+1):
                    maps[i][j] = color
        elif hasugu[0] <= mid and mid < hasugu[1]: #오른쪽 위
            #하수구있는 사분면 채우기
            color += 1
            for i in range(0,mid+1):
                for j in range(mid+1,int(2**k)):
                    maps[i][j] = color
        if mid < hasugu[0] and hasugu[1] <= mid: #왼쪽 아래
            #하수구있는 사분면 채우기
            color += 1
            for i in range(mid+1,int(2**k)):
                for j in range(0,mid+1):
                    maps[i][j] = color
        if mid < hasugu[0] and mid < hasugu[1]: #오른쪽 아래
            #하수구있는 사분면 채우기
            color += 1
            for i in range(mid+1,int(2**k)):
                for j in range(mid+1,int(2**k)):
                    maps[i][j] = color

        nx = [0,1,0,-1]
        ny = [1,0,-1,0]
        #꼭지점 별로 채우기
        for item in ggog:
            color += 1
            if maps[item[0]][item[1]] == 0:
                maps[item[0]][item[1]] = color
            for i in range(4):
                px = item[0] + nx[i]
                py = item[1] + ny[i]
                if 0 <= px < int(2**k) and 0 <= py < int(2**k) and maps[px][py] == 0:
                    maps[px][py] = color

        #하수구 채우기
        maps[hasugu[0]][hasugu[1]] = -1

        #나머지 빈칸 채우기
        color += 1
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == 0:
                    maps[i][j] = color

#맵출력
for item in maps:
    for i in range(len(item)):
        print(item[i],end="")
        if i < len(item)-1:
            print(" ",end="")
    print("")
