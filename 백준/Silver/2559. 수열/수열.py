import sys
input = sys.stdin.readline

N,K = map(int,input().split())
dayTem = list(map(int,input().split()))
sum = 0

def sumlist(numList):
    global sum

    for num in numList:
        sum+=num
    
    return sum

#초기값 저장
ragDay=[]
for k in range(K):
    ragDay.append(dayTem[k])

maxv = sumlist(ragDay)

for i in range(1,N):
    if i+K-1 < N:
        sum-=ragDay[0]
        del ragDay[0]

        sum+=dayTem[i+K-1]
        ragDay.append(dayTem[i+K-1])

        maxv = max(maxv,sum)    
    
    
print(maxv)