from collections import deque
import sys

def dfs(v):
    # 방문한 곳은 1 넣기
    visited1[v] = 1
    print(v, end=" ")

    # v와 인접한 곳을 찾고 방문하지 않았으면 함수 실행
    for i in range(1, n + 1):
        if visited1[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque()
    visited2[v] = 1
    queue.append(v)
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            if visited2[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited2[i] = 1


n, m, v = map(int, sys.stdin.readline().split())  # 정점 개수, 간선 개수, 시작 노드
graph = [[0] * (n + 1) for _ in range(n + 1)]  # n+1 x n+1 2차원 배열

# 방문 여부 초기화
visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)

# 인접한 그래프 입력 받기
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)