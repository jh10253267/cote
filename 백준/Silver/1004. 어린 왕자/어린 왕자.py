import math
T = int(input()) # 테스트 케이스의 개수

for _ in range(T): # 테스트케이스 수만큼 반복
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        departure_dist = math.sqrt((x1 - cx)**2 + (y1 - cy)**2) # 인접한 궤도와의 거리
        arrival_dist = math.sqrt((x2 - cx)**2 + (y2 - cy)**2) # 궤도와 도착점 사이의 거리

        if (arrival_dist < r) != (departure_dist < r):
            count += 1

    print(count)
