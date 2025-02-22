def solution(name):
    # 각 알파벳 변경에 필요한 조작 횟수 계산
    answer = 0
    n = len(name)
    
    # 좌우 이동 최소값 구하기
    min_move = n - 1  # 최초 최소 이동횟수는 그냥 오른쪽으로 쭉 가는 경우
    
    for i in range(n):
        # 알파벳 변경 횟수 추가
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
            
        # 현재 위치에서의 최소 이동 계산
        # 1. 왼쪽으로 갔다가 오른쪽
        # 2. 오른쪽으로 갔다가 왼쪽
        min_move = min([
            min_move,
            2 * i + n - next,  # 왼쪽으로 갔다가 오른쪽으로
            i + 2 * (n - next)  # 오른쪽으로 갔다가 왼쪽으로
        ])
    
    answer += min_move
    return answer