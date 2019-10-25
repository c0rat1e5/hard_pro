n = int(input()) + 1
a, k = 0, 1
while k < n:
    t = k * 10
    a += n // t * k + min(k, max(0, n % t - k))
    k = t
print(a)
