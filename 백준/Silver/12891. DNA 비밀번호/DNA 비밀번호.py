s, p = map(int, input().split())
dna = input()
checklist = list(map(int, input().split()))

# 초기화
start = 0
end = p - 1
count = 0
mylist = [0, 0, 0, 0]  # A, C, G, T의 개수를 저장

# 첫 번째 윈도우 설정
for i in range(p):
    if dna[i] == 'A':
        mylist[0] += 1
    elif dna[i] == 'C':
        mylist[1] += 1
    elif dna[i] == 'G':
        mylist[2] += 1
    elif dna[i] == 'T':
        mylist[3] += 1

# 조건 확인 함수
def check():
    for i in range(4):
        if mylist[i] < checklist[i]:
            return False
    return True

# 첫 번째 윈도우 검사
if check():
    count += 1

# 슬라이딩 윈도우
while end < s - 1:
    # 윈도우 이동
    end += 1
    start_char = dna[start]
    end_char = dna[end]
    start += 1

    # 윈도우 업데이트
    if start_char == 'A':
        mylist[0] -= 1
    elif start_char == 'C':
        mylist[1] -= 1
    elif start_char == 'G':
        mylist[2] -= 1
    elif start_char == 'T':
        mylist[3] -= 1

    if end_char == 'A':
        mylist[0] += 1
    elif end_char == 'C':
        mylist[1] += 1
    elif end_char == 'G':
        mylist[2] += 1
    elif end_char == 'T':
        mylist[3] += 1

    # 조건 확인
    if check():
        count += 1

print(count)
