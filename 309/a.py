"""
1 から 9 までの数字が書かれた 3×3 の盤面があります。
1 以上 9 以下の整数 A,B が与えられます。ただし、A<B です。
A が書かれたマスと B が書かれたマスが左右に隣接しているか判定してください。
"""
A, B = map(int, input().split())
if A == 3 and B == 4 or A == 6 and B == 7:
    print("No")
elif B - A == 1:
    print("Yes")
else:
    print("No")
