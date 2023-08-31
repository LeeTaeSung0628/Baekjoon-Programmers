"""
아이디어: 1. num배열의 앞에서 부터 K+1개만큼 가져온다
        2. 그중 가장 큰수를 찾고, 앞으로 올수있게 앞에값을 제거한다. k는 제거한 수만큼 줄어든다.
            2.1 k+1개의 수 중 가장 큰 수를 찾는다.
            2.2 가장큰수의 index값보다 작은 값들을 없앤다.
            2.3 없앤 수만큼 k를 줄인다.
            2.4 이때 가장 큰수가 맨앞에 있으면 그 수는 넘어간다.
        3.k가 0이되면 멈춘다.
"""

def solution(number, k):
    answer = str(number)
    i=0
    while i<len(answer)-1 and k>0 :
        if answer[i]< answer[i+1]:
            answer=answer[:i]+answer[i+1:]

            k=k-1
            if i>0:
                i=i-2
            else:
                i=i-1
        i=i+1


    if k>0 :
        answer=answer[:len(answer)-k]

    return answer
