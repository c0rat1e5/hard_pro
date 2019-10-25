from fractions import gcd

n, d = map(int, ("2 6").split())


def dfs(n, d, dp={}):
    if d == 1:
        return 1
    if n == 0:
        return 0
    if (n, d) not in dp:
        p = sum(dfs(n - 1, d // gcd(d, x)) for x in range(1, 7))
        dp[n, d] = p / 6
    return dp[n, d]


print(dfs(n, d))
