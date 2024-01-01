import math

def solution(n):
    A = [i for i in range(2, n+1)]
    A = [0] * (n+1)
    
    for i in range(2, n+1):
        A[i] = i
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if A[i] == 0:
            continue
        for j in range(i + i, n + 1, i):
            A[j] = 0
    
    answer = n - A.count(0) + 1
    return answer