def solution(mats, park):
    max_side = 1
    for y in range(len(park)):
        for x in range(len(park[0])):
            if park[y][x] != "-1":
                park[y][x] = 0
            else:
                park[y][x] = 1
    
    for y in range(1, len(park)):
        for x in range(1, len(park[0])):
            if park[y][x] == 1:
                park[y][x] = min(park[y-1][x], park[y][x-1], park[y-1][x-1]) + 1
                max_side = max(max_side, park[y][x])

    mats.sort(reverse=True)
    
    for mat in mats:
        if mat <= max_side:
            return mat
    
    return -1