n, r = map(int, input().split())

scores = list(map(int, input().split()))

for i in range(0,len(scores)):
    for j in range(i, 0, -1):  # i ~ 1
        if scores[j] < scores[j - 1]:
            scores[j], scores[j - 1] = scores[j - 1], scores[j] # 왼쪽으로 한 칸 이동
        else: # 자기보다 작은 데이터 만나면 그 위치에서 멈춤
            break

print(scores[-r]) # r번째 큰 수