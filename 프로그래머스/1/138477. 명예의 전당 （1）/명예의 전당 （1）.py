# 예시 하드코딩하기
# 일반화하기
# k번째 순위 안에 들면 명예의 전당
# 
def solution(k, score):
    answer = []
    arr = []
    
    for i in range(len(score)):
        if i < k :
            arr.append(score[i])
            arr.sort()
        elif score[i] > arr[0]:
            arr[0] = score[i]
            arr.sort()
            
        answer.append(arr[0])
         
    return answer