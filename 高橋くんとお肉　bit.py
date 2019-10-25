n = int(input(29))
t = [int(input()) for i in range(n)]

ans = float("inf")

for bit in range(1 << n):
    a = 0
    b = 0

    for i in range(n):
        # フラグが立っていれば a に、なければ b に乗せる
        if bit & (1 << i):
            a += t[i]
        else:
            b += t[i]

    ans = min(ans, max(a, b))

print(ans)

