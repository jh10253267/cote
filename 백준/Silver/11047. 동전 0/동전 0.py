n, k = map(int, input().split())
arr = [0] * n

for i in range(n):
    arr[i] = int(input())

count = 0

for i in range(n-1, -1, -1):
    if arr[i] <= k:
        count += int(k / arr[i])
        k = k % arr[i]
        
print(count)