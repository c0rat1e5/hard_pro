from collections import deque
from enum import Enum
import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001


N, W = map(int, input().split())

dp = [-1] * (W + 1)
dp[0] = 0

for loop in range(N):
    value, weight = map(int, input().split())
    for i in range(weight, W + 1):
        if dp[i - weight] == -1:
            pass
        else:
            dp[i] = max(dp[i], dp[i - weight] + value)

ans = 0
for i in range(W + 1):
    ans = max(ans, dp[i])

print("%d" % (ans))
