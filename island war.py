def solve():
    n, _, *t = map(int, open(0).read().split())
    r = [n + 1] * (n + 1)
    for a, b in zip(*[iter(t)] * 2):
        r[a] = min(r[a], b)
    a = 0
    cur = n + 1
    for i in range(n + 1):
        cur = min(cur, r[i])
        if i == cur:
            # 追いついた
            cur = r[i]
            a += 1
    print(a)


if __name__ == "__main__":
    solve()
