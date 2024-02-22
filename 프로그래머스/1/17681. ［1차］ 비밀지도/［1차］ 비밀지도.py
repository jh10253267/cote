# 정사각형 배열형태 공백 또는 벽(#)
# 두 지도 arr1, arr2가 주어지고 어느 하나라도 벽이면 실제로 벽이고
# 두개다 공백이면 전체 지도에서도 공백이다.
# 전처리 필요
# 리턴하는 값은 두개의 지도를 합친 완성된 지도를 #과 " "이용해 나타낸 것.
def solution(n, arr1, arr2):
    map =  [
            bin(i | j)[2:].zfill(n).replace("1", "#").replace("0", " ")
            for i, j in zip(arr1, arr2)
        ]
    answer = map
    return answer