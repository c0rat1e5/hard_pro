from bisect import bisect_left


def longest_increasing_sequence(arr):
    # 最長増加列の長さ
    dp = [arr[0]]
    for i in arr[1:]:
        if dp[-1] < i:
            dp.append(i)
        else:
            dp[bisect_left(dp, i)] = i
    print(len(dp))


_ = input()
arr = list(map(int, input().split()))
longest_increasing_sequence(arr)
