import sys
input = sys.stdin.readline

N = int(input())
userList = []

for i in range(N):
    x,y = list(map(str, input().split()))
    l = []
    l.append(int(x))
    l.append(y)
    l.append(int(i))
    userList.append(l)

userList.sort(key= lambda x : (x[0],x[2]))

for i in range(N):
    print(userList[i][0],userList[i][1])