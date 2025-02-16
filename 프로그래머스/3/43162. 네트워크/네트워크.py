# 모든 경로를 탐색하고 실행 횟수가 몇 회인지 확인
import sys
sys.setrecursionlimit(10**6)

def dfs(start, computers, visited):
    visited[start] = True
    
    for i, val in enumerate(computers[start]):
        if i == start:
            continue
        if val == 1 and not visited[i]:
            dfs(i, computers, visited)
    

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for start, flag in enumerate(visited):
        if not flag:
            dfs(start, computers, visited)
            answer += 1
    
    return answer