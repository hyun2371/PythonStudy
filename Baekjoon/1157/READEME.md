### 문제

[1157번: 단어 공부](https://www.acmicpc.net/problem/1157)
<br><br>

### 문제 요약

가장 많이 사용된 알파벳 대문자로 출력

여러 개일 경우 ? 출력
<br><br>

### 슈도 코드

s 대문자로 입력받기

s 집합으로 중복 없애기 → s_ele

s 원소수 세서 저장 → s_cnt
<br><br>

s_ele 최다 빈도수 →max_n

s_ele 에서 max(s_cnt)개수 세기

여러 개 → ? 출력

1개 → max_n의 위치의 원소 출력