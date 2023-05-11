### 문제

[https://www.acmicpc.net/problem/2178](https://www.acmicpc.net/problem/2178)

<br>

### 문제 요약

N X M 미로

1 이동 가능 0 이동 불가

(N,M)으로 이동하는 최단거리

<br>

### 문제 아이디어
출처 : https://www.youtube.com/watch?v=7C9RgOcvkvo&t=2721s&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
<br>

(1, 1) 위치에서 시작한다.
<br>

<img src="https://postfiles.pstatic.net/MjAyMzA1MTFfNzUg/MDAxNjgzNzg1OTU1MzQ5.tL_7WQdjIFBdeUyt-Rt4d-rEywAbhYBwLwh6jQkh2eEg.f4rGPbw0xKAjQcTEKUkEtDj1qw3n9cqv5ARP9ldfNiQg.PNG.loveanna1207/image.png?type=w773" width="200">

<br>

(1, 1) 좌표에서 상하좌우 탐색을 진행하면 옆 노드인 (1,2) 위치의 노드를 방문한다.
<br> 새롭게 방문하는 (1, 2) 노드 값을 +1해준다.
<br>

<img src="https://postfiles.pstatic.net/MjAyMzA1MTFfMzEg/MDAxNjgzNzg2MDAzMjQ2.Q1bHpq9qXRlCk5wZnWRtZzb9UWZkFwaon7-jHsAHIn4g.y9U-M6MKAOJg7w_ukVuu2aeU94YVuPw5I815We0MMo0g.PNG.loveanna1207/image.png?type=w773" width="200">

<br>

BFS를 계속 수행하면 최단 경로의 값들이 1씩 증가한다.
<br>

<img src="https://postfiles.pstatic.net/MjAyMzA1MTFfODkg/MDAxNjgzNzg2MDE2Njgy.wN8MWBYeJ9oTsx4M3rLprjMK5GOzQvNYAKSm6HZjpwAg.FNatwqvZYH6gQ0xdsqBhFehfKA66YVEhYsKUUphEHtog.PNG.loveanna1207/image.png?type=w773" width="200">