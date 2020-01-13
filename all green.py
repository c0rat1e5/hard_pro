d, g = map(int, input().split())

p = []
c = []

for i in range(d):
    a, b = map(int, input().split())
    p.append(a)
    c.append(b)

sum = []
for i in range(d):
    sum.append((i + 1) * 100 * p[i] + c[i])


def ans(g, t):
    if t <= 0:
        return 100000000000
    n = min(int(g / (100 * t)), p[t - 1])
    s = 100 * t * n

    if n == p[t - 1]:
        s = sum[t - 1]
    if g > s:
        n += ans(g - s, t - 1)

    return min(n, ans(g, t - 1))


print(ans(g, d))
