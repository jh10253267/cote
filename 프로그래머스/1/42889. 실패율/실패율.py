def solution(N, stages):
    answer = []
    temp = {}
    
    stages.sort()

    for stage in range(1, N + 1):
        user_count = 0
        unsolved_count = 0
        
        for actual in stages :
            if stage <= actual :
                user_count += 1
            if stage == actual :
                unsolved_count += 1
                
        if user_count == 0:
            temp[stage] = 0  # 분모가 0이면 실패율을 0으로 처리
        else:
            temp[stage] = unsolved_count / user_count
    
    sorted_items_descending = sorted(temp.items(), key=lambda x: x[1], reverse=True)
    
    for key in sorted_items_descending:
        answer.append(key[0])
    
    return answer
