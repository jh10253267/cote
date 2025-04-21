from itertools import combinations

graph = []

N, M = map(int, input().split())

chickens = []
houses = []
result = 65000

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chickens.append((i, j))
        elif graph[i][j] == 1:
            houses.append((i, j))

targets = list(combinations(chickens, M))

def calculate(target):
    total = 0
    for x, y in houses:
        min_distance = 100
        for cx, cy in target:
            distance = abs(x-cx)+abs(y-cy)
            min_distance = min(min_distance, distance)
        total += min_distance
    return total

def search():
    global result
    for target in targets:
        total = calculate(target)
        result = min(result, total)

search()
print(result)