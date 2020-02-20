import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 右端が右のものから処理 → 左端が狭義昇順になるようにすればよい → ただのLIS
# 右端が同じ場合：左端が大きい方から並べておく

from operator import itemgetter

N = int(readline())
m = map(int, read().split())
LR = [(x - r, x + r) for x, r in zip(m, m)]

LR.sort(key=itemgetter(0), reverse=True)
LR.sort(key=itemgetter(1), reverse=True)

seq = [x for x, y in LR]


def LIS(seq, wider_sense=True):
    from bisect import bisect_left, bisect_right
    f = bisect_right if wider_sense else bisect_left
    N = len(seq)
    INF = 10**18
    dp = [INF] * (N + 1)
    for x in seq:
        i = f(dp, x)
        dp[i] = x
    return f(dp, INF - 1)


answer = LIS(seq, wider_sense=False)
print(answer)
