# 중복을 허용하지 않는 리스트
def solution(nums):
    answer = 0
    length = len(nums) // 2
    result = []
    for i in nums :
        if i not in result:
            result.append(i)
    if len(result) >= length :
        return length;
    else:
        return len(result)
    return 