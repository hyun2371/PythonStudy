s = input().upper()  # 입력받는 문자열
s_ele = list(set(s))  # 문자열 원소
s_cnt = []  # 문자열 원소 빈도

for i in s_ele:
    s_cnt.append(s.count(i))

max_n = max(s_cnt)  # 최다 빈도수
if s_cnt.count(max_n) > 1:  # 최대 빈도 문자가 여러 개
    print('?')
else:
    max_ind = s_cnt.index(max_n)  # 최대 빈도 문자의 인덱스
    print(s_ele[max_ind])
