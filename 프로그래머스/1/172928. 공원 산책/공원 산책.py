def solution(park, routes):
    s_y = s_x = 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                s_y, s_x = i, j
                
    y, x = s_y, s_x
    route_dict = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}
    
    for route in routes:
        direction, distance = route.split()
        dy, dx = route_dict[direction]
        distance = int(distance)
        
        temp_y, temp_x = y, x
        cancel_flag = False
        
        for _ in range(distance):
            ny = temp_y + dy
            nx = temp_x + dx
            
            if ny < 0 or ny >= len(park) or nx < 0 or nx >= len(park[0]) or park[ny][nx] == "X":
                cancel_flag = True
                break
                
            temp_y, temp_x = ny, nx
            
        if not cancel_flag :
            y, x = temp_y, temp_x
            
    return [y, x]