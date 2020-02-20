n, s, k = map(int, input().split())
mod = 10 ** 9 + 7


s -= n * ((n - 1) * k) // 2


def div_num(s, n):
    dp = (s + 1) * [1]
    for i in range(2, n + 1):
        for j in range(i, s + 1):
            µ
            dp[j] = (dp[j] + dp[j - i]) % mod
    return dp[-1]


if s < 0:
    print(0)
else:
    print(div_num(s, n))
