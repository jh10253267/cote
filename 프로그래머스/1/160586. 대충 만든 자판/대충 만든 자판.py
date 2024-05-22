## 최소값 갱신해서 사용하기
def solution(keymap, targets):
    answer = []
    key_dict = {}
    
    for char in keymap:
        for c in char:
            if c in key_dict:
                key_dict[c] = min(char.index(c) + 1, key_dict[c])
            else:
                key_dict[c] = char.index(c) + 1
    
    for target in targets:
        sum = 0
        flag = False
        for t in target:
            if t not in key_dict:
                flag = True
                break
            else:
                sum += key_dict[t]
        if flag:
            answer.append(-1)
        else :    
            answer.append(sum)
    
    return answer