# 1벽 2바이러스 0빈방
N, M = map(int, input().split()) # 세로, 가로
data = []
graph = [[0] * M for _ in range(N)]
result = 0

for i in range(N):
    data.append(list(map(int, input().split())))

dx = [0, 0, -1, 1] # 상하좌우
dy = [-1, 1, 0, 0]

def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                score += 1
    return score

def infect(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and ny >= 0 and nx < M and ny < N:
            if graph[ny][nx] == 0:
                graph[ny][nx] = 2
                infect(nx, ny)
    
def dfs(count):
    global result
    if count == 3:
        for y in range(N):
            for x in range(M):
                graph[y][x] = data[y][x]
                    
        for y in range(N):
            for x in range(M):
                if data[y][x] == 2:
                    infect(x, y)
        result = max(result, get_score())
        return
        
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
    
dfs(0)
print(result)