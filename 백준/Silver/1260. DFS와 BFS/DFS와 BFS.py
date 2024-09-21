import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())

lst = [[] for _ in range(n + 1)]
visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)
queue = deque()

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

def dfs(start, visited, lst):
    visited[start] = True
    print(start, end=' ')
    for i in sorted(lst[start]):
        if not visited[i]:
            dfs(i, visited, lst)

def bfs(start, visited, lst):
    queue.append(start)
    visited[start] = True
    while queue:
        start = queue.popleft()
        print(start, end=' ')
        for i in sorted(lst[start]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(v, visited1, lst)
print()
bfs(v, visited2, lst)