# 그냥 다 조합해보고 중복제거, 정렬
# 시간복잡도 약 O(n^2)

def solution(numbers):
    answer = []
    numbers.sort()
    result = []
    
    length = len(numbers)
    for i in range(length - 1):
        for j in range(i+1, length) :
            result.append(numbers[i] + numbers[j])    
    result = set(result)
    result = list(result)
    result.sort()
    return result