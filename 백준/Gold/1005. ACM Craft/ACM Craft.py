from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    # 건물 별 걸리는 시간 기록
    d = [0] + list(map(int, input().split()))
    arr = [[] for _ in range(n + 1)]
    # 건물의 차수를 저장
    degree = [0] * (n+1)

    # 입력을 받은 뒤 연결리스트로 연결 정보를 기록하고 차수를 기록한다.
    for _ in range(k):
        x, y = map(int, input().split())
        arr[x].append(y)
        degree[y] += 1
        
    w = int(input())
    time = [0] * (n+1)
    
    # 큐 선언
    q = deque()

    # 처음 시작 시 정렬을 시작할 노드를 반복문을 돌며 추가가
    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
            time[i] = d[i]

    # 큐가 전부 빌 때까지 반복
    while q:
        now = q.popleft() 
        
        for i in arr[now]:
            degree[i] -= 1
            time[i] = max(time[now] + d[i], time[i])
            if degree[i] == 0:
                q.append(i)
        if now == w:
          break
    print(time[w])