
K, S = [1400, 2000]
count = 0
for x in range(K + 1):
    for y in range(K + 1):
        z = S - x - y
        if 0 <= z <= K:
            count += 1
print(count)
