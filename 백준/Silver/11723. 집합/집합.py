import sys
input = sys.stdin.readline

S = 0b0
n = int(input())
for _ in range(n):
    item = input().split()
    if len(item) > 1:
        x = int(item[1])
    if item[0] == "add":
        S = S | (1 << x)
    elif item[0] == "remove":
        S = S & ~(1 << x)
    elif item[0] == "toggle":
        S = S ^ (1 << x)
    elif item[0] == "check":
            chk = S & (1 << x)
            if chk == 0:
                print("0")
            else:
                print("1")
    elif item[0] == "all":
        S = 0b111111111111111111111
    elif item[0] == "empty":
        S = 0b0