N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = []

for i in range(N):
    su = A[i]
    while num <= su:
        stack.append(num)
        answer.append("+")
        num += 1
    if stack[-1] == su:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        result = False
        break

if result:
    for op in answer:
        print(op)
