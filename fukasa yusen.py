from collections import deque

def iterative_dfs():
    H, W = map(int, input().split())
    edges = ['#'] * (W + 2)
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    field = [edges]
    for i in range(H):
        line = input()
        field.append(['#'] + list(line) + ['#'])
        if 's' in line:
            sx, sy = i + 1, line.index('s') + 1
    field.append(edges)

    s = deque()
    push, pop = s.append, s.pop
    push((sx, sy))
    while s:
        cx, cy = pop()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if field[nx][ny] == '#':
                continue
            if field[nx][ny] == 'g':
                print('Yes')
                exit()
            push((nx, ny))
            field[nx][ny] = '#'
    print('No')


if __name__ == '__main__':
    iterative_dfs()
