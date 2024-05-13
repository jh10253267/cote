def solution(s, skip, index):
    answer = ''
    al = "abcdefghijklmnopqrstuvwxyz"
    for ch in skip:
        al = al.replace(ch, "")
        
    for i in s:
        answer += al[(al.index(i) + index) % len(al)]
    return answer