from collections import deque

answer = 0

def BFS(maps, x, y):
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[-1][-1]

def solution(maps):
    if BFS(maps, 0, 0) > 1:
        answer = BFS(maps, 0, 0)
    else:
        answer = -1
        
    return answer