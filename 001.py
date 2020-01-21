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


ni(3)
na(2 0 3 1 1 3)
ns(4 2 0 4 5 5)
