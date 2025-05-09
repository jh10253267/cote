
def solution(N, number):
    if N == number:
        return 1
    
    answer = 0
    flag = False
    dp = [set() for _ in range(9)]
    dp[1].add(N)
    
    for i in range(2, 9):
        dp[i].add(int(str(N)*i))
        
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
            
            if number in dp[i]:
                flag = True
                answer = i
                break
        if flag:
            break
    
    if answer == 0:
        return -1
    else:
        return answer