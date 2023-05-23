import sys

input = sys.stdin.readline

bitList = [ input().strip() for _ in range(2)]

size = len(bitList[0])

for i in range(len(bitList)):
    bitList[i] = int(bitList[i],2)

print(format(bitList[0] & bitList[1], 'b').zfill(size))
print(format(bitList[0] | bitList[1], 'b').zfill(size))
print(format(bitList[0] ^ bitList[1], 'b').zfill(size))
b1 = format(bitList[0], 'b').zfill(size)
b2 = format(bitList[1], 'b').zfill(size)
res1 = ""
for item in b1:
    if item == "0":
        res1 += "1"
    else:
        res1 += "0"
res2 = ""
for item in b2:
    if item == "0":
        res2 += "1"
    else:
        res2 += "0"

print(res1)
print(res2)