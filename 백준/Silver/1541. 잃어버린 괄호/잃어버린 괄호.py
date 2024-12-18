arr = list(map(str, input().split("-")))
result = 0


def sum_func(str):
    sum = 0
    temp = str.split("+")
    
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(arr)):
    temp = sum_func(arr[i])
    if i == 0:
        result += temp
    else:
        result -= temp

print(result)