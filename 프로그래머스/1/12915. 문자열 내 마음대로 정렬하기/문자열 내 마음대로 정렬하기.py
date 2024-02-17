def solution(strings, n):
    # 각 문자열의 n번째 문자를 기준으로 정렬한다.
    answer = []
    temp = []
    
    for i in strings:
        temp.append(i[n] + i)
    temp_sorted = sorted(temp)
    for i in temp_sorted:
        answer.append(i[1:])    
    
    return answer