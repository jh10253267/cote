# 예시 하드코딩
# 문제 풀이 시나리오 짜기
# 첫번째 사진 메이, 케인, 카인, 라디 점수 5+10+1+3 
# 두번재 사진 메이, 케인, 브린, 데니 점수 5+10
# 세번째 사진 콘 케인 메이 코니 점수 5+1 
# 정답 [19, 15, 6]
def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    answer = []
    for names in photo:
        score = 0
        for name in names:
            if name in dic:
                score += dic[name]
        answer.append(score)
    return answer