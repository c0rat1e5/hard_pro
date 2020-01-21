import sys
stdin = sys.stdin


def ni():
    return int(ns())


def na():
    return list(map(int, stdin.readline().split()))


def ns():
    return stdin.readline()


n = ni()
red = []
for _ in range(n):
    red.append(na())
blue = []
for _ in range(n):
    blue.append(na())

red.sort()
blue.sort()
ans = 0

tmp = []
for i in blue:
    for j in red:
        if i[0] > j[0] and i[1] > j[1]:
            tmp.append(j)
    if tmp != []:
        max_red = max(tmp, key=lambda x: x[1])
        ans += 1
        red.remove(max_red)
        tmp = []
    else:
        pass

print(ans)
