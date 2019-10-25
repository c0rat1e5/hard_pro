N = int(input())
red = [list(map(int, input().split())) for _ in range(N)]
blue = [list(map(int, input().split())) for _ in range(N)]
red.sort(reverse=True, key=lambda x: x[1])
blue.sort()
ans = 0
for b in blue:
    for r in red:
        if r[0] < b[0] and r[1] < b[1]:
            red.remove(r)
            ans += 1
            break
print(ans)
