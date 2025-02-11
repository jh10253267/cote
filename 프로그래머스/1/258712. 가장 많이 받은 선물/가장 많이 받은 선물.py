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
    
    gift_count = [0] * n
    
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
                
            g_cout = g_arr[i][j]
            t_cout = g_arr[j][i]
            # 서로 주고받았지만 동수가 아닌 경우
            if g_cout > t_cout:
                gift_count[i] += 1
            # 서로 주고받았지만 동수인 경우
            elif g_cout==t_cout and g_score[j] < g_score[i]:
                if g_cout > 0:
                    gift_count[i] += 1
                elif g_cout == 0:
                    gift_count[i] += 1
                    
    return max(gift_count)