from collections import deque

def solution(s):
    dq = deque(s)
    answer = 0

    if len(s) % 2 != 0:
        return 0

    for i in range(len(s)):
        if check_func(dq):
            answer += 1
        
        dq.append(dq.popleft())

    return answer

def check_func(dq):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}

    for ch in dq:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()

    return not stack