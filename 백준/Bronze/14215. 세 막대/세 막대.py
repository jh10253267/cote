arr = list(map(int, input().split()))
arr.sort()
result = 0
w = 0

if arr[-1] >= arr[0] + arr[1]:
    w = arr[0] + arr[1] - 1
else:
    w = arr[-1]

result = w + arr[0] + arr[1]

print(result)