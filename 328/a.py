"""
N 問の問題が出題されるプログラミングコンテストがあります。 
i=1,2,…,N について、i 問目の配点は Siです。配点が X 以下である問題すべての配点の合計を出力してください。
"""
N, X = map(int, input().split())
S = list(map(int, input().split()))
ans = 0

for s in S:
    if s <= X:
        ans += s

print(ans)
