# 1. 문제 이해 
# section 칠해야하는 구역
# n 섹션 번호
# m 롤러 미터
# 2. 가공
# 3. 하드코딩
# 4. 일반화

def solution(n, m, section):
    answer = 0
    temp = 0
    count = 0
    for i in section:
        if temp >= i :
            continue;    
        temp = i + m - 1
        count += 1
        
    answer = count
    return answer