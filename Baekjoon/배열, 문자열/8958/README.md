### 문제

[8958번: OX퀴즈](https://www.acmicpc.net/problem/8958)
</br></br>
### 문제 요약

n 입력 받는 테스트 케이스 개수

연속된 O의 개수로 점수 합산

OX 퀴즈

OOXXOXXOOO

1+2+1+1+2+3 → 10

한 줄 마다 계산해서 출력
</br>
</br>

### 슈도 코드

n 번 반복

s = int(input())

total = 0

s 길이만큼 반복

r = 연속된 O

i) O → r +=1

ii) X →   r = 0

total += r