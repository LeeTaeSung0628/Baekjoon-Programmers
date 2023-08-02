import string
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

inputText = input().rstrip()
answer = int(1e9)
size = len(inputText)

#입력한 위치부터 팰린드롬이 있는지 확인한다
def checkPalindrome(isPalindrome, inputText, startIndex, endIndex):
    size = len(inputText)
    while 0 <= startIndex and endIndex < size and inputText[startIndex] == inputText[endIndex]:
        isPalindrome[startIndex][endIndex] = True
        startIndex -= 1
        endIndex += 1

def getIsPalindrome(inputText):
    size = len(inputText)
    isPalindrome = [[False] * size for _ in range(size)]

    for startIndex in range(size):
        #홀수길이
        checkPalindrome(isPalindrome, inputText, startIndex, startIndex)
        #짝수길이
        checkPalindrome(isPalindrome, inputText, startIndex, startIndex + 1)
            
    return isPalindrome

isPalindrome = getIsPalindrome(inputText)

DP = [1] * size
for rightIndex in range(1, size):
    #초기값은 이전 결과 + 1
    DP[rightIndex] = DP[rightIndex - 1] + 1
    for leftIndex in range(rightIndex):
        #만약 팰린드롬이 있을 경우
        if isPalindrome[leftIndex][rightIndex]:
            #leftIndex가 0일때 팰린드롬인 경우 무조건 최솟값이기 때문에 break
            if leftIndex == 0:
                DP[rightIndex] = 1
                break
            else:
                #현재값과 팰린드롬 이전의 결과+1 중 작은 값을 저장
                DP[rightIndex] = min(DP[rightIndex], DP[leftIndex - 1] + 1)

print(DP[size - 1])