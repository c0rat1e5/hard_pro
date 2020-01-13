a = [input() for i in range(10)]
sea = 0
for i in a:
    sea += i.count("x")
par, rank = [i for i in range(101)], [0 for i in range(101)]


def root(x):
    if par[x] != x:
        par[x] = root(par[x])
    return par[x]


def unite(x, y):
    x2, y2 = root(x), root(y)
    if x2 != y2:
        if rank[x2] < rank[y2]:
            par[x2] = y2
        else:
            par[y2] = x2
        if rank[x2] == rank[y2]:
            rank[x2] += 1


def nei(x, y):
    L = []
    for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if -1 < i < 10 and -1 < j < 10:
            L.append([i, j])
    return L


for i in range(10):
    for j in range(10):
        if a[i][j] == "o":
            for k, k2 in nei(i, j):
                if a[k][k2] == "o":
                    unite(i * 10 + j + 1, k * 10 + k2 + 1)
R = set()
for i in range(1, 101):
    R.add(root(i))
isl = len(R) - sea
if isl == 1:
    ans = "YES"
elif isl > 4:
    ans = "NO"
else:
    ans = "NO"
    for i in range(10):
        for j in range(10):
            if a[i][j] == "x":
                b = set()
                for k, k2 in nei(i, j):
                    if a[k][k2] == "o":
                        b.add(root(k * 10 + k2 + 1))
                if len(b) == isl:
                    ans = "YES"
print(ans)
