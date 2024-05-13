# 중복되는 값과 그 갯수 찾기, 최댓값 찾기 -> 최댓값의 조건은 큰 수부터 나열하는 것.
def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))
    
    if len(answer) == 0:
        answer = "-1"
    elif len(answer) == answer.count('0'):
        answer = "0"    
    return answer