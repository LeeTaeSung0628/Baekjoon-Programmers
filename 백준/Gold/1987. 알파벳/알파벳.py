import sys 
from collections import deque
input=sys.stdin.readline
R,C = map(int, input().split())
arr=[list(input()) for _ in range(R)]
check=[0]*(26)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
maxi=0

def dfs(x,y,cnt):
    global maxi
    maxi=max(cnt,maxi)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<R and ny<C and nx>=0 and ny>=0 and check[ord(arr[nx][ny])-65]==0:
            check[ord(arr[nx][ny])-65]=1
            ncnt=cnt+1
            dfs(nx,ny,ncnt)
            check[ord(arr[nx][ny])-65]=0

check[ord(arr[0][0])-65]=1
dfs(0,0,1)

print(maxi)