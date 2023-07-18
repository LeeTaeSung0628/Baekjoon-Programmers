from collections import deque

n, dong = map(int, input().split())
visited = [0] * 100001 #방문했는지 안했는지

q = deque([(n, 0)]) #현재 위치 / 현재 위치로 올 수 있는 최단시간
fast, way = 10 ** 6, 0
# fast : 최단시간
# way : 경우의수
while q:
  now, time = q.popleft() 
  visited[now] = 1 #방문처리
  #동생을 만났거나, 현재누적시산이 작거나 같을때 누구랑? 최단시간이랑
  if now == dong and time <= fast:
    #최단시간 갱신
    fast = min(fast, time)
    #경로 추가
    way += 1
#누적시간이 최단시간보다 크면 멈추기
  if time > fast: break


  for x in (now - 1, now + 1, now * 2):
    if x in range(100001) and not visited[x]:
      q.append((x, time + 1))
  
print(fast)
print(way)