from collections import deque

def solution(n, stations, w):
    answer = 0
    queue = deque(stations)

    position = 1
    while position <= n:
        if len(queue) > 0 and queue[0] - w <= position: 
            position = queue.popleft() + w + 1
        else:
            answer += 1
            position += 2 * w + 1

    return answer