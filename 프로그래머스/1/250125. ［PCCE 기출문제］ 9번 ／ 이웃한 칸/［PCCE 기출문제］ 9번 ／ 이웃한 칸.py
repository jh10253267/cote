# 격자 보드에서 상하좌우중 같은 색이 칠해진 칸의 갯수 구하기
# w는 x좌표 h는 y좌표
# 탐색 순서는 오른쪽, 아래, 위, 왼쪽 
def solution(board, h, w):
    answer = 0
    dh = [1, -1, 0, 0]
    dw = [0, 0, 1, -1]
    target = board[h][w]
    
    for i in range(len(dh)):
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < len(board) and 0 <= w_check < len(board):
            if board[h_check][w_check] == target:
                answer += 1
    return answer