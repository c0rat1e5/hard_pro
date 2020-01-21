T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

flag = True

q = 0

for i, b in enumerate(B):
    # if B has more remainings than A does, then there would not be enough takoyaki.
    if len(B) - i > len(A) - q:
        flag = False
        break
    found = False
    for j in range(q, len(A)):
        if A[j] <= b and b <= A[j] + T:
            q = j + 1
            found = True
            break
    if found is False:
        flag = False
        break
if flag:
    print("yes")
else:
    print("no")
