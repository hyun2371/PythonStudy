s = input().strip()
space_cnt = 0
for i in s:
    if i == ' ':
        space_cnt += 1
print(space_cnt + 1)  # 단어의 개수 = 공백의 개수+1
