from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
arr.reverse()
result = []

for i in arr:
    idx = bisect_left(result, i)

    if idx == len(result):
        result.append(i)
    else:
        result[idx] = i

print(N - len(result))