import sys
input = sys.stdin.readline

gualList = list(input().rstrip()) # rstrip() 함수는 "\n" 줄바꿈 문자열을 제거해 준다.
G_stack = []
leftCnt = 0 #스텍에 남은 '(' 개수
totalCnt = 0 # 막대기 개수
for i in gualList:
    if i == "(":
        G_stack = i
        leftCnt+=1
        totalCnt+=1
    else:
        if G_stack == "(":
            G_stack = ")"
            leftCnt-=1
            totalCnt-=1
            totalCnt =  totalCnt + leftCnt
        else:
            G_stack = ")"
            leftCnt-=1

print(totalCnt)