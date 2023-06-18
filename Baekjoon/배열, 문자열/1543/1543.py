# 영어로만 이뤄진 문서를 검색하는 함수
# 어떤단어가 몇번 등작했는지

s = input()
k = input()
result = 0

i = 0 # s 인덱스
while i < len(s):
    if s[i:i + len(k)] == k:
        result += 1
        i = i + len(k) # k칸만큼 건너뜀
    else:
        i += 1

print(result)
