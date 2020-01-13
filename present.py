def solve():
    from bisect import bisect_left
    from sys import stdin
    f_i = stdin

    N = int(f_i.readline())

    wh = []
    for i in range(N):
        w, h = map(int, f_i.readline().split())
        h *= -1
        wh.append((w, h))
    wh.sort()

    # LIS
    pre_w, pre_h = wh[0]
    pre_h *= -1
    H = [pre_h]
    for w, h in wh[1:]:
        h *= -1
        if h > H[-1]:
            H.append(h)
        else:
            j = bisect_left(H, h)
            H[j] = h

    print(len(H))


solve()
