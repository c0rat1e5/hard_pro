s = set()
s.add(0)
n = int((3))
l = list(map(int, ("10 5 6").split()))
for x in l:
    n = set()
    for t in s:
        n.add(t + x)
    s |= n
print(len(s))
