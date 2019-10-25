n, k, *a = map(int, open(0).read().split())
t, s = 2**40, 0
while t:
    c = sum((i & t) // t for i in a)
    if k < t or c * 2 >= n:
        s += t * c
    else:
        s += t * (n - c)
        k -= t
    t //= 2
print(s)
