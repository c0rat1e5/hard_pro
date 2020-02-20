n = int(input())
point = [-1] * 394
for _ in range(n):
    s, l, p = map(int, input().split())
    for i in range(s, l + 1):
        point[i] = max(point[i], p)

for i in range(394):
    for j in range(i):
        point[i] = max(point[i], point[j] + point[i - j])

m = int(input())
ans = []
for _ in range(m):
    ans.append(point[int(input())])
if -1 in ans:
    print(-1)
else:
    print(*ans, sep="\n")
