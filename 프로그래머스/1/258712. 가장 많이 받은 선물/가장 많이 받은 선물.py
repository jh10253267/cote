def solution(friends, gifts):
    n = len(friends)
    g_arr = [[0] * len(friends) for _ in range(n)]
    t_arr = [0] * n
    g_score = [0] * n
    
    for gift in gifts:
        giver, taker = gift.split()
        g_idx = friends.index(giver)
        t_idx = friends.index(taker)
        
        g_arr[g_idx][t_idx] += 1
        t_arr[t_idx] += 1
    
    for i in range(n):
        g_score[i] = sum(g_arr[i]) - t_arr[i]
    
    max_gift = [0] * n
    
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
                
            g_cout = g_arr[i][j]
            t_cout = g_arr[j][i]
            
            if g_cout > t_cout:
                max_gift[i] += 1
            # 서로 주고받았지만 동수인 경우
            elif (g_cout > 0 and t_cout > 0) and (g_cout==t_cout):
                if g_score[j] < g_score[i]:
                    max_gift[i] += 1
            # 서로 주고받은 적이 없다.
            elif (g_cout == 0 and t_cout == 0) and (g_score[j] < g_score[i]):
                max_gift[i] += 1
            
                
    return max(max_gift)