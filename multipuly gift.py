x, y = map(int, ("3 20").split())

ans = 0

while x <= y:
    x *= 2
    ans += 1

print(ans)
