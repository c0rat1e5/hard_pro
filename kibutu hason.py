from collections import deque

def bfs(grid, sy, sx, target, wall):
    grid[sy][sx] = wall
    queue = deque([])
    queue.append([sy, sx, 0])
    dxy = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        y,x,cnt = queue.popleft()
        if cnt > 2:
            break
        for dy, dx in dxy:
            y_,x_ = y+dy,x+dx
            if grid[y_][x_] == target:
                return cnt
            if grid[y_][x_] == wall:
                continue
            if grid[y_][x_] == '#':
                queue.append([y_,x_,cnt+1])
            else:
                queue.appendleft([y_,x_,cnt])
            grid[y_][x_] = wall
    return 3

H,W = map(int, input().split())
wall = '_'
start = 's'
goal = 'g'
edges = [wall for i in range(W+2) ]
grid = [edges]
for i in range(1,H+1):
    S = [wall] + list(input().strip()) + [wall]
    if start in S:
        sy, sx = i, S.index(start)
    grid.append(S)
grid.append(edges)

print('YES' if bfs(grid, sy, sx, goal, wall) <= 2 else 'NO')
