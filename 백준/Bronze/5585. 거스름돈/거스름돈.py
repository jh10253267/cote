N = 1000 - int(input())

cash = [500 ,100, 50, 10, 5, 1]
answer = 0

for c in cash:
    if N >= c:
        answer += N // c
        N = N % c

print(answer)