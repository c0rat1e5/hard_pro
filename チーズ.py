from collections import deque


def bfs(sx, sy, gx, gy):
    d = [[float("inf")] * w for i in range(h)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    que.append((sx, sy))
    d[sx][sy] = 0

    while que:
        p = que.popleft()
        if p[0] == gx and p[1] == gy:
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if 0 <= nx and nx < h and 0 <= ny and ny < w and\
                    maze[nx][ny] != "X" and d[nx][ny] == float("inf"):
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d[gx][gy]


h, w, n = map(int, ('10 10 9').split())
maze = [list(".X...X.S.X")]
maze += [list("6..5X..X1X")]
maze += [list("...XXXX..X")]
maze += [list("X..9X...X.")]
maze += [list("8.X2X..X3X")]
maze += [list("...XX.X4..")]
maze += [list("XX....7X..")]
maze += [list("X..X..XX..")]
maze += [list("X...X.XX..")]
maze += [list("..X.......")]


# 各チーズ工場の座標
g = [0] * n
for i in range(h):
    for j in range(w):
        if maze[i][j] == "S":
            sx = i
            sy = j
        # 書かれているのが数字なら g にその座標を書き込む
        if maze[i][j].isdecimal():
            g[int(maze[i][j]) - 1] = (i, j)

# 1回目は巣をスタート、硬さ1のチーズ工場をゴールにする
ans = bfs(sx, sy, g[0][0], g[0][1])
# それ以降は前回の工場をスタート、次の工場をゴールにする
for i in range(1, n):
    ans += bfs(g[i - 1][0], g[i - 1][1], g[i][0], g[i][1])
print(ans)
print(sx)
