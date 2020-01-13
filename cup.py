
p3, c = [1]*16, [0]*16

for i in range(1, 16):
    p3[i] = 3*p3[i-1]
while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    for i in range(3):
        a = list(map(int, input().split()))
        for j in range(a[0]):
            c[a[j+1]-1] = i
    ans = k = 0;
    for i in range(n):
        j = c[i]-k
        if j < 0: j = -j
        ans += j*p3[n-i-1]
        if j == 1: k = 2-k
    k = p3[n]-ans-1
    if ans > k: ans = k
    print(ans if ans <= m else -1)

