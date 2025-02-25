def solution(name):
    answer = 0
    length = len(name)
    start = 65
    end = 90
    min_val = length-1
    
    for i, val in enumerate(name):
        answer += min(end-ord(val)+1, ord(val)-start)
        next = i+1
        while next < length and name[next] == 'A':
            next += 1
            
        min_val = min(min_val,
                     i*2 + length-next,
                     i + 2*(length-next))
    answer += min_val
    return answer