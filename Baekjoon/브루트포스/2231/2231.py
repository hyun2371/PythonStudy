n = int(input())
ans = 0  # 생성자 없으면 0 출력

for k in range(1, n):
    total = sum((map(int, str(k))))
    total += k
    if total == n:
        ans = k
        break

print(ans)

