# 최고 순위와 최저 순위 배열로 리턴
def solution(lottos, win_nums):
    answer = []
    zero_count = 0
    win_count = 0
    for i in lottos:
        if i == 0:
            zero_count += 1
        for j in win_nums:
            if i == j :
                win_count += 1
    highest = 7 - (win_count + zero_count)
    
    if highest == 7:
        highest = 6
        
    if win_count == 0 :
        lowest = 6
    else:    
        lowest = 7 - win_count
    
    answer.append(highest)
    answer.append(lowest)
    
    return answer