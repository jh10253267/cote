from queue import PriorityQueue
n = int(input())

plus_queue = PriorityQueue()
minus_queue = PriorityQueue()
one = 0
zero = 0

for i in range(n):
    data = int(input())
    if data>1:
        plus_queue.put(data * -1)
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        minus_queue.put(data)
sum = 0

while plus_queue.qsize() > 1:
    first = plus_queue.get() * -1
    second = plus_queue.get() * -1
    sum += first * second

if plus_queue.qsize() > 0:
    sum += plus_queue.get() * -1

while minus_queue.qsize() > 1:
    first = minus_queue.get()
    second = minus_queue.get()
    sum += first * second

if minus_queue.qsize() > 0:
    if zero == 0:
        sum += minus_queue.get()
sum += one

print(sum)