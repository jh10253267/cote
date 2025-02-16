# 탐색문제
# 하나의 노드당 +, - 둘다 실행을 해봐야한다.
# 별도의 함수를 호출했을 경우 어떻게 결괏값을 넘겨받을 수 있을지
def dfs(data, answer, depth, result, target):
    if depth == len(data):
        if result == target:
            answer[0] += 1
    else:
        dfs(data, answer, depth+1, result+data[depth], target)
        dfs(data, answer, depth+1, result-data[depth], target)
    
def solution(numbers, target):
    answer = [0]
    depth = 0
    result = 0
    dfs(numbers, answer, depth, result, target)
    return answer[0]