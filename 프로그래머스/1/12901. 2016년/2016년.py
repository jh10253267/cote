# 요일은 7일을 주기로 반복된다.
def solution(a, b):
    answer = ''
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0
    
    for i in range(a) :
        sum += days[i]
        # 31+ 29
    sum = (sum - days[a-1]) + b
    # 60 - 29 + 1 = 32
    # 32 % 7 = 4
    answer = day[sum % 7-1]
    
    return answer