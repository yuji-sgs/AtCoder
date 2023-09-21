"""
正整数 X が与えられます。 X 以下の最大のべき乗数を求めてください。 
ただし、べき乗数とは、ある 1 以上の整数 b と 2 以上の整数 p を使って b^pとかける整数のことを指すこととします。
"""
X = int(input())
max_num = 1
for i in range(1, int(X**0.5) + 1):
    for j in range(2, X + 1):
        if i**j > X:
            break 
        max_num = max(max_num, i**j)

print(max_num)
