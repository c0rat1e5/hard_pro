

n, m = map(int, input().split())
dp = [[[0 for z in range(101)] for y in range(101)] for x in range(101)]
for i in range(n):
    x, y, z, w = map(int, input().split())
    dp[x][y][z] = max(dp[x][y][z], w)
for x in range(101):
    for y in range(101):
        for z in range(101):
            dp[x][y][z] = max(dp[x][y][z], dp[max(0, x - 1)][y][z],
                              dp[x][max(0, y - 1)][z], dp[x][y][max(0, z - 1)])
for k in range(m):
    x, y, z = map(int, input().split())
    print(dp[x][y][z])
