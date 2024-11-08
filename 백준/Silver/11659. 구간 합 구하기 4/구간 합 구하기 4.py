import sys
input = sys.stdin.readline

numbers_length, query_length = map(int, input().split())
numbers = list(map(int, input().split()))
temp = 0
prefix_sum = [0]

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(query_length):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
