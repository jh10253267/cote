# 1. 문제 이해하기
# 2. 데이터 가공
# 3. 하드코딩
# 4. 일반화
from itertools import combinations
import math
def solution(nums):
    answer = 0
    temp = list(combinations(nums, 3))
    count = 0
    for i in temp:
        result = sum(i)
        div_count = 0
        for j in range(2, result):
            if(result % j == 0):
                div_count += 1      
        if(div_count == 0):
            answer += 1
    return answer