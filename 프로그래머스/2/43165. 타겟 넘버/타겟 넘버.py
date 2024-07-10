def DFS(depth, max_depth, numbers, result, target, answer):
    if depth == max_depth:
        if result == target:
            answer[0] += 1
    else:
        DFS(depth + 1, max_depth, numbers, result + numbers[depth], target, answer)
        DFS(depth + 1, max_depth, numbers, result - numbers[depth], target, answer)

def solution(numbers, target):
    max_depth = len(numbers)
    answer = [0]  # 리스트를 사용하여 변경 가능한 객체로 만듭니다.
    DFS(0, max_depth, numbers, 0, target, answer)
    return answer[0]  # 리스트의 첫 번째 요소를 반환합니다.
