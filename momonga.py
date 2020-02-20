import sys
from sys import stdin
input = stdin.readline

import heapq


def dijkstra(V, to, start, goal, x):
    Q = []
    visited = [0] * V
    heapq.heappush(Q, (-x, start))
    while Q:
        t, s = heapq.heappop(Q)
        t = -t
        if s == goal:
            return x + h[goal] - t * 2
        if visited[s]:
            continue
        visited[s] = 1
        for e, c in to[s]:
            if visited[e] or c > h[s]:
                continue
            d = min(h[e], t - c)
            heapq.heappush(Q, (-d, e))
    return -1


n, m, x = map(int, input().split())
h = [int(input()) for i in range(n)]
to = [[] for i in range(n)]
for i in range(m):
    a, b, t = map(int, input().split())
    a, b = a - 1, b - 1
    to[a].append((b, t))
    to[b].append((a, t))
print(dijkstra(n, to, 0, n - 1, x))
