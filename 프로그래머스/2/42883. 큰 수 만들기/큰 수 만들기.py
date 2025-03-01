def solution(number, k):
    answer = ''
    stack = []
    limit = len(number) - k
    arr = list(map(int, number))
    
    for num in arr:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
            print("!!")
        stack.append(num)
        print(stack)
        
    return "".join(map(str, stack))