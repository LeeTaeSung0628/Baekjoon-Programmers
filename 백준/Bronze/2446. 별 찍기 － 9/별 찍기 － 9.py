import sys
input = sys.stdin.readline

N = int(input())

i=N-1
while i > 0:
    zz = (" " * ((N-1)-i)) + ("*" + "*" * (2*i))
    print(zz)
    i-=1

for i in range(N):
    zz = (" " * ((N-1)-i)) + ("*" + "*" * (2*i))
    print(zz)