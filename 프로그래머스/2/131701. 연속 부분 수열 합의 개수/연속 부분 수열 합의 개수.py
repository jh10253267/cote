def solution(elements):
    answer = set()
    n = len(elements)
    elements += elements
    
    for step in range(1, n+1):
        now = sum(elements[:step])
        answer.add(now)
        for i in range(1, n):
            now = now - elements[i-1] + elements[i+step-1]
            answer.add(now)
        
    return len(answer)