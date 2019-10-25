c = list(map(int, ().split()))
a = int(380)

# コインの金額
v = [1, 5, 10, 50, 100, 500]
ans = 0

for i in range(1, 7):
    t = min(a // v[-i], c[-i])  # コイン i を使う枚数
    a -= t * v[-i]
    ans += t

print(ans)

