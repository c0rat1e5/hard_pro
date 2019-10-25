t = int(("3"))

for i in range(t):
    s = ("""higashikyoto
        kupconsitetokyotokyoto
        goodluckandhavefun""")
    ans = 0
    j = 0

    while j < len(s) - 4:
        # 前から5文字ずつ見ていく
        if s[j:j + 5] == "tokyo" or s[j:j + 5] == "kyoto":
            ans += 1
            # 一致すれば5文字分進める
            j += 5
        else:
            j += 1

    print(ans)
