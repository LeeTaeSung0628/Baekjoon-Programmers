import sys
input = sys.stdin.readline

"""
    아이디어 : 거꾸로 한글짜씩 줄인다!
            수가 같아지면 비교하고 같으면 1 다르면 0
"""
#초기값
s = input().strip()
t = list(input().strip())

#정방향인지(0) 뒤집혔는지(1)
check = 0
while len(t) > len(s):
    if check == 0: #정방향이면
        ch = t.pop() #마지막글자 빼기
    else: #뒤집혔으면
        ch = t.pop(0) #첫글짜 빼기

    if ch == "B": # B면 뒤집기
        if check == 1: check = 0
        else: check = 1

sumST = ""
if check == 0:#정방향이면
    for i in range(len(t)):
        sumST += t[i]
else: #뒤집혔으면
    l = len(t)-1
    for i in range(len(t)):
        sumST += t[l-i]

if sumST == s:
    print(1)
else: print(0)