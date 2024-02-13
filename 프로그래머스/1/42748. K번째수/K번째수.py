# 1. 문제 이해하기
# 2. 데이터 가공하기
# 3. 하드코딩
# 4. 일반화
def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0]
        end = i[1]
        k = i[2]
        
        temp = array[start-1:end]
        temp.sort()
        answer.append(temp[k-1])
            
    return answer