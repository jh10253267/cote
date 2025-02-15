def solution(board, h, w):
    answer = 0
    dh = [1, -1, 0, 0] # 상하
    dw = [0, 0, 1, -1] # 좌우
    target = board[h][w]

    for i in range(len(dh)):
      h_check, w_check = h + dh[i], w + dw[i]

      if 0 <= h_check < len(board) and 0 <= w_check < len(board[0]):
        if board[h_check][w_check] == target:
          answer += 1

    return answer