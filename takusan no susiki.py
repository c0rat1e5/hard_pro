s = input()
a = []
sbox = []

for i in s:
    a.append(int(i))

n = len(a)


def f(i, box, k):
    if i == n - 1:
        box += k
        sbox.append(box)
    else:
        f(i + 1, box + k, a[i + 1])
        f(i + 1, box, 10 * k + a[i + 1])

f(0, 0, a[0])
print(sum(sbox))
