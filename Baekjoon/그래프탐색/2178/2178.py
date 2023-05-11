import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph=[]

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

# 이동할 네 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간 벗어난 경우 무시
            if nx <= -1 or nx >=n or ny <= -1 or ny >= m:
                continue
            # 이동할 수 없는 칸인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 거리 측정
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0, 0))