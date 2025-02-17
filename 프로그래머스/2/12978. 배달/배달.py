import heapq

def dijkstra(start, distance, graph):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(N, road, K):
    INF = int(1e9)
    answer = 0
    graph = [[] for i in range(N+1)]
    distance = [INF] * (N+1)
    
    for i in road:
        graph[i[1]].append((i[0], i[2]))
        graph[i[0]].append((i[1], i[2]))
    
    dijkstra(1, distance, graph)
    
    for i in distance:
        if i <= K:
            answer += 1
    return answer