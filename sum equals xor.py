s = ("").strip()
mod = 10**9 + 7
r, l = 1, 1
for c in s[::-1]:
    r, l = 3 * r % mod, (r + 2 * l) % mod if int(c) else l
print(l)
