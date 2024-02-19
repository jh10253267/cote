N = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

# 포인터가 이동하는 조건
# sum이 N과 같을 경우 end_index++
# sum이 N보다 큰 경우 start_index++

while end_index != N:
    if sum == N:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > N :
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index
        
print(count)