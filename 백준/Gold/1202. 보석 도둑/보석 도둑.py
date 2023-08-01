
import sys
import heapq
input = sys.stdin.readline

N, K = map(int,input().split())
zual = [list(map(int,input().split())) for _ in range(N)]
pack = [int(input()) for _ in range(K)]

#최적해 : 가장 비싼보석을 가능한 작은 가방에 넣어야한다

#무게가 가벼운 순으로 정렬
zual.sort()
pack.sort()

total = 0

q = []

for p in pack:
    #가방을 하나씩 꺼내서 넣을수 있는 애들을
    #우선순위 큐에 넣는다
    while zual and p >= zual[0][0]:
        #가격이 가장 작은애들부터 탐색하고, 못넣으면 멈춘다.
        #만약 넣었다면 크기가 가장작은애니까, pop해준다
        heapq.heappush(q,[-zual[0][1],zual[0][1]])
        heapq.heappop(zual)

    if len(q) != 0:
        _, price = heapq.heappop(q)
        total += price
                   
print(total)