def solution(prices):
    length = len(prices)
    answer = [0] * length
    for i in range(length):
        for j in range(i+1, length):
            if prices[i] <= prices[j]:
                answer[i] += 1
            # 그렇지 않은 경우
            else:
                answer[i] += 1
                break
            
    return answer