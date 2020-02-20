from bisect import*
b = bisect_left
n, *t = map(int, open(0).read().split())
l = [1e9] * n
for _, w in sorted(zip(t[::2], t[1::2]),
                   key=lambda x: (x[0], -x[1])): l[b(l, w)]=w
print(b(l, 1e9))
