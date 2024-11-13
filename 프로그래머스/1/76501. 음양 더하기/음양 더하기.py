def solution(absolutes, signs):
    answer = 0
    for i, num in enumerate(absolutes):
        if not signs[i]:
            num = num * -1

        answer = answer + num  
    return answer