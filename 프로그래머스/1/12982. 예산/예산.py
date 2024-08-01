def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    for i in d:
        sum += i
        if sum <= budget:
            answer += 1
    
    return answer