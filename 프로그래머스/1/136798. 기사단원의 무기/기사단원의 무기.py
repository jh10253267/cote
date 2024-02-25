import math

def solution(number, limit, power):
    temp = []
    for i in range(1, number+1) :
        count = 0
        for j in range(1, int(math.sqrt(i)) + 1):
            if(i % j == 0):
                count += 1
                if j ** 2 != i:
                    count += 1
        temp.append(count)        
    answer = 0
    for i in temp:
        if(i > limit) :
            answer += power
        else:
            answer += i
    return answer