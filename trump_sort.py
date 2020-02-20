from bisect import*
n, *c = map(int, open(0))
l = []
for i in c:
    j = bisect(l, i)
    if len(l) == j:
        l.append(i)
    else:
        l[j] = i
print(n - len(l))
