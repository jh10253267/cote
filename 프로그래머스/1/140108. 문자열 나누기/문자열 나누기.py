def solution(s):
    answer = 0
    pre_char = ''
    pre_count = 0
    count = 0
    index = 0
    for char in s:
        if len(pre_char) == 0:
            if(index == len(s) - 1):
                answer += 1
            else:
                pre_char = char
                pre_count += 1
        else:
            if pre_char == char:
                pre_count += 1
            else:
                count += 1
                if count == pre_count:
                    pre_count = 0
                    count = 0
                    answer += 1
                    pre_char = ''
        if index == len(s) -1 and (pre_count != count):
            answer += 1
        index += 1
    return answer