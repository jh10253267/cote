n = int(input())
arr = [[0]*2 for i in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    arr[i][0] = b
    arr[i][1] = a

arr.sort()

end = -1
count = 0

for i in range(n):
    if arr[i][1] >= end:
        end = arr[i][0]
        count += 1

print(count)