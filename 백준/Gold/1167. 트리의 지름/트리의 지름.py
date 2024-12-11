from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
array = [[] for _ in range(v+1)]

for _ in range(v):
    data = list(map(int, input().split()))
    index = 0
    s = data[index] # 노드
    index += 1 # 연결 노드의 인덱스
    while True:
        e = data[index] # 연결 노드의 번호
        if e == -1:
            break
        w = data[index+1] # 연결 노드와의 거리
        array[s].append((e, w))
        index += 2

distance = [0] * (v+1)
visited = [False] * (v+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        for i in array[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                q.append(i[0])
                distance[i[0]] = distance[now] + i[1]

bfs(1)
max = 1

for i in range(2, v+1):
    if distance[max] < distance[i]:
        max = i

distance = [0] * (v+1)
visited = [False] * (v+1)
bfs(max)
distance.sort()
print(distance[v])