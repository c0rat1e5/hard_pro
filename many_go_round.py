def ii(): return int(input())


def mi(): return map(int, input().split())


def li(): return list(map(int, input().split()))


n, m, l, x = mi()
a = li()
inf = 10 ** 9 + 7
dp = [inf] * m
dp[0] = 0
sup = x * m
import numpy as np
dp = np.array(dp)
for i in range(n):
    nokori = a[i] % m
    hiki = m - nokori
    dpp = np.concatenate([dp[hiki:], dp[:hiki]], 0) + int(a[i])
    dp = np.minimum(dp, dpp)
if dp[l] < sup:
    print("Yes")
else:
    print("No")
