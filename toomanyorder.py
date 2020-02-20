import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

MOD = 10**9 + 7

N, M, Q = map(int, readline().split())
A = list(map(int, readline().split()))
KX = np.array(read().split(), np.int32)
K = KX[::2]; X = KX[1::2]

# 形式的べき級数やるだけ！

dp = np.zeros(M + 1, np.int64)
dp[0] = 1

for n in A:
    # 1+x+...+x^nをかける。1-x^{n+1} をかけていく
    dp[n + 1:] -= dp.copy()[:-(n + 1)]
    dp %= MOD

# 1-xでN-1回割る → どうせあとでひとつかけるので
for _ in range(N - 1):
    np.cumsum(dp, out=dp)
    dp %= MOD

# 1箇所だけキャンセルすることで、番号ごとのdp表を得る
# 1/(1-x^{n+1})倍する
dp1 = np.zeros((N, M + 1), np.int64)
for i, n in enumerate(A):
    # dpを(1+x^{n+1}+....)倍したものをdp1[i]に入れる
    L = (M + 1) + (-M - 1) % (n + 1)
    dp1[i] = np.resize(dp, L).reshape(-1, n +
                                      1).cumsum(axis=0).ravel()[:M + 1] % MOD

answer = dp1[K - 1, M - X]

print('\n'.join(answer.astype(str)))
