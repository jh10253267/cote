def solution(wallpaper):
    data = []
    answer = []
    for row_idx, column in enumerate(wallpaper):
        for i in range(len(column)):
            if column[i] == "#":
                data.append((row_idx, i))
    
    row_idx_min = len(wallpaper)
    row_idx_max = -1
    i_min = len(wallpaper[0]) - 1
    i_max = -1
    
    for row_idx, i in data:
        row_idx_min = min(row_idx_min, row_idx)
        i_min = min(i_min, i)
        row_idx_max = max(row_idx_max, row_idx)
        i_max = max(i_max, i)
        
    answer.extend([row_idx_min, i_min, row_idx_max + 1, i_max + 1])
    return answer