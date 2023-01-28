### 문제

[2675번: 문자열 반복](https://www.acmicpc.net/problem/2675)
</br></br>
### 문제 요약

문자열 S 입력 받기

각 문자 R번 반복해 문자열 P를 만든 후 출력

3 ABC

5 /HTP 

AAABBBCCC

/////HHHHHTTTTTPPPPP
</br></br>
### 슈도 코드

n 입력 받기

n 번 반복

3 ABC → map(r, s)

s 원소만큼 반복

s원소 * int(r)