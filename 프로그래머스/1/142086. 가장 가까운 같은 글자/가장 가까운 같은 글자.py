def solution(s):
    answer = []
    alp_dic = {}
    for idx, alp in enumerate(s):
        if alp not in alp_dic :
            answer.append(-1)
        else :
            answer.append(idx-alp_dic[alp])    
        alp_dic[alp] = idx    
        
    return answer