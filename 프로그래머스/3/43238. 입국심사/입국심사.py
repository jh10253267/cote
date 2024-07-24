def solution(n, times):
    min_time, max_time = 1, max(times) * n
    
    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        total = sum(mid // time for time in times)
        
        if total >= n:
            max_time = mid - 1
        else:
            min_time = mid + 1
            
    return min_time