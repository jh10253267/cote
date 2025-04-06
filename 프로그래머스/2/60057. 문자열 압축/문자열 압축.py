def solution(s):
    answer = len(s)
    
    for chunk in range(1, len(s)//2+1):
        temp = ""
        prev = s[:chunk]
        count = 1
        for i in range(chunk, len(s), chunk):
            if prev == s[i:i+chunk]:
                count += 1
            else:
                temp += str(count)+prev if count >= 2 else prev
                prev = s[i:i+chunk]
                count = 1
        temp += str(count)+prev if count >= 2 else prev
        answer = min(answer, len(temp))
    
    return answer