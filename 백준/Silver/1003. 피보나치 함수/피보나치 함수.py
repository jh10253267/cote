n = int(input())

def fibo(n):
    one_count, zero_count = 1, 1
    
    for i in range(2, n):
        temp = one_count # 1
        one_count = zero_count + one_count # 2
        zero_count = temp # 1
    
    print(zero_count, one_count)
     
for _ in range(n):
    number = int(input())
    
    if number == 0:
        print(1, 0)
    elif number == 1:
        print(0, 1)
    elif number == 2:
        print(1, 1)
    else:
        fibo(number)