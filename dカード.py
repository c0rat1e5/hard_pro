import itertools

n = 6
k = 3
card =

# set を使うと重複せずに数えられる
number = set()
# card から k 個選んで並び替える
for i in itertools.permutations(card, k):
    # 並び替えたものを繋げて1つの文字列にする
    number.add("".join(i))

print(len(number))
