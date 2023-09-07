"""
英小文字からなる文字列 S が与えられます。
S から a, e, i, o, u をすべて取り除いて得られる文字列を出力してください。
なお、S は a, e, i, o, u 以外の文字を一つ以上含みます。
"""
S = input()
ans = ""
list = ["a", "i", "u", "e", "o"]
for s in S:
    if s not in list:
        ans += s
print(ans)
