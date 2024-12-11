n, m = map(int, input().split())
array = list(map(int, input().split()))
start = max(array)
end = sum(array)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    count = 0
    for i in range(n): # 전체 수업을 순회
        if sum + array[i] > mid: # 앞에서부터 더한 값이 정한 최소크기보다 클 경우
            count += 1 # 개수를 하나 증가시키고
            sum = 0 # 누적된 합을 초기화
        sum += array[i] # 수업 길이를 하나씩 더해간다.
    if sum != 0: # 딱떨이지지 않는 경우 1시간이라도 오버되면 블루레이가 하나 더 필요하다.
        count += 1 
    if count > m: # 이진탐색
        start = mid + 1
    else:
        end = mid - 1

print(start)