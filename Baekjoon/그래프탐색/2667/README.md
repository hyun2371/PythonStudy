### 문제

[https://www.acmicpc.net/problem/2667](https://www.acmicpc.net/problem/2667)

<br>

### 문제 요약

1끼리 상하좌우로 연결 → 단지

단지 수 출력하고, 각 단지 속하는 집 수 오름차순 출력

<br>

### 슈도 코드

1. 특정 지점 상, 하, 좌, 우 살피기
2. 주변 지점 중 값이 1이면서 방문하지 않은 지점 있으면 해당 지점 방문
    
    방문한 지점에서 다시 상하좌우 살피며 방문 반복
    
    방문했을 때 값을 0으로 바꾸고 카운트 1
    
    각 단지별로 카운트 한 값을 배열에 저장한다.
    
3. 1, 2번의 과정을 반복하며, 방문하지 않은 지점을 방문한다.
4. 각 단지별 카운트를 오름차순으로 정렬한다.

<br>

### 배운점

전역 변수 사용: 변수 앞에 `global` 붙이기