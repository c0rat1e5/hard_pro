D = int(("3"))
N = map(int, ("1000"))

g = 10 ** 9 + 7
V = [0] * D
A = 0
W = [0] * (D + 10)
for i, x in enumerate(N):
    for j in range(len(W)):
        W[j] = 0

    for j, y in enumerate(V):
        if y != 0:
            W[j + 1] += y
            W[j + 10] -= y

    W[A] += 1
    W[A + x] -= 1
    s = 0
    for j, y in enumerate(W):
        s = (s + y) % g
        V[j % D] += s

    A += x
    A %= D

V[A] += 1
print((V[0] - 1) % g)
