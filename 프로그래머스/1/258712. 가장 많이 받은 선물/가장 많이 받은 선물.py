from collections import defaultdict

def solution(friends, gifts):
    n = len(friends)
    give = [defaultdict(int) for _ in range(n)]
    take = [0] * n
    gift_index = {friend: i for i, friend in enumerate(friends)}
    gift_score = [0] * n

    for gift in gifts:
        giver, taker = gift.split()
        g_idx = gift_index[giver]
        t_idx = gift_index[taker]

        give[g_idx][t_idx] += 1
        take[t_idx] += 1

    for i in range(n):
        gift_score[i] = sum(give[i].values()) - take[i]

    max_gift = 0
    for i in range(n):
        possible_gifts = 0
        
        for j in range(n):
            if i == j:
                continue
            
            if give[i][j] > give[j][i]:
                possible_gifts += 1
            elif give[i][j] == give[j][i]:
                if gift_score[i] > gift_score[j]:
                    possible_gifts += 1

        max_gift = max(max_gift, possible_gifts)

    return max_gift
