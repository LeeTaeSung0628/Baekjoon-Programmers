
import itertools

def solution(word):
     #product = 중복순열, repeat = n개의 조합
    st = ['A', 'E', 'I', 'O', 'U']
    l5 = itertools.product(st,repeat = 5) 
    l4 = itertools.product(st,repeat = 4)
    l3 = itertools.product(st,repeat = 3)
    l2 = itertools.product(st,repeat = 2)
    l1 = itertools.product(st,repeat = 1)
                
    
    #모든 경우의수 합치기
    sumL = list(l1)+list(l2)+list(l3)+list(l4)+list(l5)
    
    justL = []#자리수 채우기
    sums = ""
    for n in sumL:
        for i in range(len(n)):
            sums = sums+ n[i]
        sums = sums.ljust(5,"0")
        justL.append(sums)
        sums = ""

    #사전순으로 정렬
    justL = sorted(justL,key = lambda x : (x[0],x[1],x[2],x[3],x[4]))
        
    answer = justL.index(word.ljust(5,"0"))+1
    return answer