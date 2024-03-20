import heapq

def solution(n, paths, gates, summits):
    answer = [0, 10000001]
    summits = set(summits)
    gates = set(gates)
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        intensity[start] = 0
        while q:
            # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            if now in summits:
                continue
            # 현재 노드가 이미 처리된 적이 있는 것이면 무시
            if intensity[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들 확인
            for i in graph[now]:
                if i[0] in gates:
                    continue
                cost = max(intensity[now], i[1])
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < intensity[i[0]]:
                    intensity[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    intensity = [10000001] * (n + 1)
    for start in gates:
        dijkstra(start)

    for target in summits:
        if intensity[target] < answer[1]:
            answer = [target, intensity[target]]
        elif intensity[target] == answer[1]:
            answer[0] = min(target, answer[0])

    return answer