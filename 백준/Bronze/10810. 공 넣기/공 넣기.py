
import sys
input = sys.stdin.readline

n, m =  map(int,input().split())
shot = [list(map(int,input().split())) for _ in range(m)]

maps = ["0"] * n

for i in range(len(shot)):
    s,e,n = shot[i]
    s = s-1
    e = e-1
    for j in range(s,e+1):
        maps[j] = str(n)

print(" ".join(maps))
