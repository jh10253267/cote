import sys
sys.setrecursionlimit(10000)  # 올바른 함수 호출
input = sys.stdin.readline

N = int(input())

def isPrime(num):
    if num < 2:  # 소수가 2 이상이므로 예외 처리
        return False
    for i in range(2, int(num ** 0.5) + 1):  # 제곱근까지만 확인
        if num % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:  # 짝수는 소수가 아니므로 건너뜀
                continue
            new_number = number * 10 + i
            if isPrime(new_number):  # 소수일 때만 탐색 진행
                DFS(new_number)

# 한 자리 소수로 시작
DFS(2)
DFS(3)
DFS(5)
DFS(7)
