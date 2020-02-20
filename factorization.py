n, m = map(int, input().split())
i = 2
s = []
while i * i <= m:
  j = 0
  while m % i == 0:
    m //= i
    j += 1
  if j:
    s += [j]
  i += 1
a = 1
if m > 1:
  s += [1]

for v in s:
  c = 1
  for i in range(v):
    c = c * (n + i) // (1 + i)
  a = a * c % (10**9 + 7)
print(a)
