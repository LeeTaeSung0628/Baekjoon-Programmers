import sys
input = sys.stdin.readline

N, M, R = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
r_case = list(map(int,input().split()))

#1. 상하반전
def updown(maps):
    t_maps = []
    for i in range(len(maps)):
        t_maps.append(maps[len(maps)-1-i])
    
    return(t_maps)
        
#2. 좌우반전
def leftrigh(maps):
    t_maps = []
    for i in range(len(maps)):
        temp = []
        for j in range(len(maps[0])):
            temp.append(maps[i][len(maps[0])-1-j])
        t_maps.append(temp)

    return(t_maps)

#3. 오른쪽으로 90도 회전
def right90(maps):
    t_maps = []
    for j in range(len(maps[0])):
        temp = []
        for i in range(len(maps)):
            temp.append(maps[len(maps)-1-i][j])
        t_maps.append(temp)
    return t_maps

#4. 왼쪽으로 90도 회전
def left90(maps):
    t_maps = []
    for j in range(len(maps[0])):
        temp = []
        for i in range(len(maps)):
            temp.append(maps[i][len(maps[0])-1-j])
        t_maps.append(temp)
    return t_maps

#ex. 4개로 나누고, 돌리는 연산
def slice4(maps):
    t_maps1 = []
    t_maps2 = []
    t_maps3 = []
    t_maps4 = []

    for i in range(len(maps)//2):
        temp = []
        for j in range(len(maps[0])//2):
            temp.append(maps[i][j])
        t_maps1.append(temp)
    
    for i in range(len(maps)//2):
        temp = []
        for j in range(len(maps[0])//2,len(maps[0])):
            temp.append(maps[i][j])
        t_maps2.append(temp)

    for i in range(len(maps)//2,len(maps)):
        temp = []
        for j in range(len(maps[0])//2,len(maps[0])):
            temp.append(maps[i][j])
        t_maps3.append(temp)

    for i in range(len(maps)//2,len(maps)):
        temp = []
        for j in range(len(maps[0])//2):
            temp.append(maps[i][j])
        t_maps4.append(temp)

    return([t_maps1,t_maps2,t_maps3,t_maps4])

#5. 슬라이스 된것으로 오른쪽으로 회전
def s_right(maps):
    m1,m2,m3,m4 = slice4(maps)
    t_maps = []

    for i in range(len(maps)//2):
        t_maps.append(m4[i]+m1[i])

    for i in range(len(maps)//2):
        t_maps.append(m3[i]+m2[i])

    return t_maps

#6. 슬라이스 된것으로 왼쪽으로 회전
def s_left(maps):
    m1,m2,m3,m4 = slice4(maps)
    t_maps = []

    for i in range(len(maps)//2):
        t_maps.append(m2[i]+m3[i])

    for i in range(len(maps)//2):
        t_maps.append(m1[i]+m4[i])

    return t_maps

for item in r_case:
    if item == 1:
        maps = updown(maps)
    elif item == 2:
        maps = leftrigh(maps)
    elif item == 3: 
        maps = right90(maps)
    elif item == 4: 
        maps = left90(maps)
    elif item == 5: 
        maps = s_right(maps)
    elif item == 6: 
        maps = s_left(maps)
        
for i in range(len(maps)):
    for j in range(len(maps[0])):
        print(maps[i][j],end=" ")
    print("")

"""
6 8 1
1 1 1 1 2 2 2 2
1 1 1 1 2 2 2 2
1 1 1 1 2 2 2 2
4 4 4 4 3 3 3 3
4 4 4 4 3 3 3 3
4 4 4 4 3 3 3 3
1
"""