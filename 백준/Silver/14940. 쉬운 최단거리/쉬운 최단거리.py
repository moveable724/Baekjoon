from collections import deque

def bfs(start, graph, distance):
    queue = deque([start])
    distance[start[0]][start[1]] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

# 입력
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

# 초기화
distance = [[-1] * n for _ in range(m)]

# 시작점 찾기
start = None
for i in range(m):
    for j in range(n):
        if graph[i][j] == 2:
            start = (i, j)
        elif graph[i][j] == 0:
            distance[i][j] = 0

# BFS 실행
if start:
    bfs(start, graph, distance)

# 출력
for row in distance:
    print(" ".join(map(str, row)))
