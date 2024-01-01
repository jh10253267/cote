import sys
input = sys.stdin.readline

# 시간복잡도 최대 2000이면 2000^2 
# 수의 갯수
n = int(input())
result = 0
# 수 입력받기
a = list(map(int, input().split()))
a.sort()

for k in range(n):
    find = a[k]
    i = 0
    j = n - 1
    while i < j :
        if a[i] + a[j] == find:
            if i != k and j !=k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
            else:
                j -= 1
        elif a[i] + a[j] < find:
            i += 1
        else:
            j -= 1
print(result)