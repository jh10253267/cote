# 시전시간, 1초당 회복량, 추가 회복량
# 5초 동안 초당 1의 회복을 하며 연속 5번 회복시 추가 회복량 5
# 2초에 10만큼의 피해가 들어온다.
def solution(bandage, health, attacks):
    last_attack = attacks[-1][0]
    attacks_dict = {time: damage for time, damage in attacks}
    combo = 0
    current_health = health
    max_health = health
    for time in range(1, last_attack+1):
        if time in attacks_dict:
            current_health -= attacks_dict[time]
            combo = 0
            if current_health <= 0:
                return -1
        else:
            current_health += bandage[1]
            combo += 1
            if combo == bandage[0]:
                current_health += bandage[2]
                combo = 0
                
            current_health = min(max_health, current_health)
    
    return current_health