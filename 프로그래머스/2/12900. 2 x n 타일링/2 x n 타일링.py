def solution(n):
    # n-1까지 채워진 경우 세로로 놓는 경우의 수 1개
    # n-2까지 채워진 경우 가로로 2개를 놓는 경우의 수 1개 
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 1000000007
    
    return dp[-1]