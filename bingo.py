n, m, s = map(int, input().split())
k = n**2
ns = s - k * (k + 1) // 2
nm = m - k
p = [[-1] * (k + 1) for i in range(ns + 1)]
mod = 10**5


def calcp(ns, k):
    if ns == 0 and k == 0:
        return 1
    if ns < 0 or k <= 0:
        return 0
    if p[ns][k] != -1:
        return p[ns][k]


for i in range(ns + 1):
    for j in range(1, k + 1):
        p[i][j] = (calcp(i, j - 1) + calcp(i - j, j) -
                   calcp(i - j - nm, j - 1) + mod) % mod
print(p[ns][k])
