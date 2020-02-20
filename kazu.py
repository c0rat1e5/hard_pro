import numpy as np

_in = list(open(0))
d = int(_in[0])
n = _in[1].strip()

mod = 1000000007

A = np.zeros((d, d), dtype=np.int64)
for i in range(10):
    A[0][i % d] += 1

for i in range(1, d):
    for j in range(d):
        A[i][j] = A[i - 1][j - 1]

s = np.zeros(d, dtype=np.int64)
s_max = 0
for i in range(len(n)):
    s = np.dot(s, A) % mod
    for j in range(int(n[i])):
        s[(s_max + j) % d] += 1
    s_max += int(n[i])

s[s_max % d] += 1
print((s[0] - 1) % mod)
