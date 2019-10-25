d, n = map(int, input().split())
t = [int(input())for _ in range(d)]
ma, mi = [-1] * 61, [101] * 61
for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(a, b + 1):
        ma[j] = max(ma[j], c)
        mi[j] = min(mi[j], c)
ai = [[ma[t[i]], mi[t[i]]]for i in range(d)]
dp = [[0, 0]for i in range(d)]
for i in range(1, d):
    for j in range(2):
        dp[i][j] = max(dp[i - 1][0] + abs(ai[i - 1][0] - ai[i][j]),
                       dp[i - 1][1] + abs(ai[i - 1][1] - ai[i][j]))
print(max(dp[-1]))
