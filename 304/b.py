"""
問題文省略
https://atcoder.jp/contests/abc304/tasks/abc304_b
"""
N = input()
if len(N) <= 3:
    print(N)
else:
    print(N[:3] + "0" * (len(N) - 3))
