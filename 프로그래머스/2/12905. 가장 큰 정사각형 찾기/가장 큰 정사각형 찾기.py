def solution(board):
    max_side = board[0][0]
    rows, cols = len(board), len(board[0])

    for i in range(1, rows):
        for j in range(1, cols):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                max_side = max(max_side, board[i][j])

    return max_side ** 2
