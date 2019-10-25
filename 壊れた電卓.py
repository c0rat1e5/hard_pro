n, l = input().split()
l = int(l)


ans = float('inf')
for i in range(len(n)):
    for j in range(10):
        for k in range(10):
            num = n[:i] + str(j) + str(k) * (len(n) - i - 1)
            if num[0] == '0':
                num = num[1:]
            if len(set(num)) <= l and num:
                ans = min(abs(int(n) - int(num)), ans)


print(ans)
