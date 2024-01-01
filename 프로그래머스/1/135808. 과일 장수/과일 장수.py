# k = 최고등급
# m = 한상자에 담는 사과의 갯수
# m개씩 잘라서 가장 최솟값 * m

def solution(k, m, score):
    answer = 0
    score.sort()
    
    answer = sum(score[len(score)%m::m]) * m
    
    return answer