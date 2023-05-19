n = int(input())
result = []
for _ in range(n):
    result.append(int(input()))


for i in range(len(result)): # 첫번째 ~ 배열 길이-1
    min_ind = i
    for j in range(i+1, len(result)):
        if result[j] < result[min_ind]: # 최소값 인덱스 구하기
            min_ind = j
    result[i], result[min_ind] = result[min_ind], result[i] # j번째와 최소값 스왑

print(*result, sep = "\n")