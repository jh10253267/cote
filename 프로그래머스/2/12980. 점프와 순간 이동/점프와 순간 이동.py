# 최솟값 찾기
# 이동 방식과 최솟값 간의 연관관계 찾기
# 5의 경우 처음 한 칸 점프 -> 순간이동 결과 2로 또 순간이동 결과 4로 그다음 한 칸 점프
def solution(n):
    ans = bin(n).count('1')
    return ans