import numpy as np
N, K = map(int, input().split())
A = np.array([input() for _ in range(N)], dtype=np.int64)
Acum = np.zeros(N + 1, dtype=np.int64)
Acum[1:] = A.cumsum()

INF = 2**31 - 1
dp = np.full((N + 1, N + 1), INF, dtype=np.int64)
dp[1, 0] = 0
dp[1, 1] = 1

for n in range(2, N + 1):
    dp[n] = dp[n - 1]
    x = Acum[n - 1]
    y = Acum[n]
    dp[n, 1:] = np.minimum(dp[n, 1:], 1 + y * dp[n - 1, :-1] // x)

answer = np.searchsorted(dp[N], K, side='right') - 1
if K == Acum[-1]:
    answer = 1
print(answer)
