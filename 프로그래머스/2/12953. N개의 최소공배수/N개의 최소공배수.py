import math

def lcm(a, b):
    return a*b // math.gcd(a, b)

def solution(arr):
    answer = lcm(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        answer = lcm(answer, arr[i])
    
    return answer