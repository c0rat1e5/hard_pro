MOD = 10**9 + 7

n = int(input())
k = int(input())


def getComb(n, k, MOD):
    if n - k < k:
        k = n - k
    comb = 1
    for x in range(n - k + 1, n + 1):
        comb *= x
        comb %= MOD
    d = 1
    for x in range(1, k + 1):
        d *= x
        d %= MOD
    comb *= pow(d, MOD - 2, MOD)
    return comb % MOD


ans = getComb(n + k - 1, k, MOD)
print(ans)
