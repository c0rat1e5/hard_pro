N, Y = [10, 45000]
for x in range(N + 1):
    for y in range(N - x + 1):
        z = N - x - y
        if x * 10000 + y * 5000 + z * 1000 == Y:
            print(x, y, z)
            exit()
print(-1, -1, -1)
