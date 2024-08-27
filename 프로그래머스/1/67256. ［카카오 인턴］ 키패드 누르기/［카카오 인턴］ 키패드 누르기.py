# 간단하게 1, 4, 7 왼손, 3, 6, 9면 오른손
# 만약 중간에 해당하는 2, 5, 8, 0이라면 현재 키패드에서 더 가까운 손 사용 그러기 위한 변수 hand
# 거리가 같다면 오른손, 왼손잡이냐에 따라 달라진다.
# 5의 경우 이전 손의 위치는 왼쪽 오른쪽 각각 4, 3으로 5와 거리가 가까운 손은 왼손
def dist(position1, position2):
    y1, x1 = position1
    y2, x2 = position2
    return abs(y2 - y1) + abs(x2 - x1)
    
def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    left_hand = dic['*']
    right_hand = dic['#']
    
    for num in numbers:
        if num in [1, 4, 7]:
            left_hand = dic[num]
            answer += "L"
        elif num in [3, 6, 9]:
            right_hand = dic[num]
            answer += "R"
        else:
            if dist(right_hand, dic[num]) < dist(left_hand, dic[num]):
                right_hand = dic[num]
                answer += "R"
            elif dist(right_hand, dic[num]) > dist(left_hand, dic[num]):
                left_hand = dic[num]
                answer += "L"
            else:
                if hand == "right":
                    right_hand = dic[num]
                    answer += "R"
                else:
                    left_hand = dic[num]
                    answer += "L"
                
    return answer