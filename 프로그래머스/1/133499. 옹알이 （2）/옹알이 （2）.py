def solution(babbling):
    answer = 0
    target = {"aya", "ye", "woo", "ma"}
    
    for word in babbling:
        if word in target:
            answer += 1
        else:
            comp = ""
            prev_comp = ""
            temp = "" 
            for char in word:
                if temp in target:
                    if temp != comp:
                        if prev_comp != temp:
                            comp += temp
                            prev_comp = temp
                            temp = ""
                
                temp += char
            
            if comp == temp or prev_comp == temp:
                continue
                
            elif temp in target:
                if comp != temp:
                    comp += temp
                    prev_comp += temp
                
            if word == comp:
                answer += 1
    return answer