import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [[] for _ in range(n+1)]
visited = [False] * (n+1)
arrive = False

def dfs(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in array[now]:
        if not visited[i]:
            dfs(i, depth + 1)
    visited[now] = False

for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

for i in range(n):
    dfs(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)