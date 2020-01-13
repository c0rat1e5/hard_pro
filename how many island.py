import sys
sys.setrecursionlimit(10000)


def f(x, y):
    if 0 <= x < w and 0 <= y < h and a[y][x] == '1':
        a[y][x] = '0'
        for dx, dy in[[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]:
            f(x + dx, y + dy)


while 1:
    w, h = map(int, input().split())
    if w == 0:
        break
    a = [input().split() for _ in[0] * h]
    b = 0
    for i in range(w):
        for j in range(h):
            if a[j][i] == '1':
                b += 1
                f(i, j)
    print(b)
