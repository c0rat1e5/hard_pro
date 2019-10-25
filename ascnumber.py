n = int(input())
a = 1
for i in range(9):
    a = a * (n + 1 + i)
for j in range(9):
    a = a // (j + 1)
print(a % (10**9 + 7))
