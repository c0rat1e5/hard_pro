def bfs():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    field = [list(input()) for _ in range(r)]
    tests = ((0, 1), (1, 0), (-1, 0), (0, -1))

    start_point = (sy-1, sx-1)
    goal_point = (gy-1, gx-1)
    field[start_point[0]][start_point[1]] = 0
    queue = [start_point]
    moves = 0

    while queue:
        queue_next = []
        moves += 1
        for y, x in queue:
            for ny, nx in tests:
                ty, tx = y + ny, x + nx
                if field[ty][tx] == '.':
                    field[ty][tx] = moves
                    queue_next.append((ty, tx))
        queue = queue_next
        if goal_point in queue:
            break

    print(moves)


if __name__ == "__main__":
    bfs()
