
import sys
input = sys.stdin.readline

st = list(input().strip())
boom = list(input().strip())


#스텍에 삽입하다가, 폭발문자열이 맨뒤부터 폭발문자열만큼 체크해서 같다면 삭제
stack = []
for item in st:
    #스텍에 문자열 삽입
    stack.append(item)

    #폭발 문자열 수보다 크거나 같다면 체크
    if len(stack) >= len(boom):
        #폭발문자열체크(뒤부터)
        matchCnt = 0 #폭탄의 길이와 같으면 없애기
        for i in range(len(boom)):
            if boom[len(boom)-1 -i] == stack[len(stack)-1 -i]:
                matchCnt +=1
        #폭탄이 발견되면(개수가 폭탄의 길이와 같다면)
        if matchCnt == len(boom):
            for _ in range(matchCnt):
                stack.pop()

if len(stack) < 1:
    print("FRULA")
else:print("".join(stack))