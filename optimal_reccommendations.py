import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# a,b,cが小さいので全部埋めればよい

import numpy as np

N, M = map(int, readline().split())
data = np.array(read().split(), np.int32)

dp = np.zeros((101, 101, 101), np.int32)

A, B, C, W = data[:4 * N].reshape(N, 4).T
ind = W.argsort()
A = A[ind]
B = B[ind]
C = C[ind]
W = W[ind]

dp[A, B, C] = W

np.maximum.accumulate(dp, axis=0, out=dp)
np.maximum.accumulate(dp, axis=1, out=dp)
np.maximum.accumulate(dp, axis=2, out=dp)

X, Y, Z = data[4 * N:].reshape(M, 3).T
answer = dp[X, Y, Z]
print('\n'.join(answer.astype(str)))
