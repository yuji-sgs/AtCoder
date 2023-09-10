"""
高橋くんは回転寿司で N 皿の料理を食べました。 i 皿目の色は文字列 C iで表されます。
また、料理の価格は皿の色と対応し、 i=1,…,M のそれぞれについて、色が文字列 Diの皿の料理は一皿 Pi円です。
また、D1,…,DMのいずれとも異なる色の皿の料理は一皿 P0円です。
高橋くんが食べた料理の価格の合計を求めてください。
"""

N, M = map(int, input().split())
C = input().split()
D = input().split()
prices = list(map(int, input().split()))

# P0とそれ以外の価格に分ける
P0 = prices[0]
P = prices[1:]

# 色と価格の辞書を作成
color_price_dict = {}
for i in range(M):
    color = D[i]
    price = P[i]
    color_price_dict[color] = price

# 食べた皿の合計価格を計算
total_price = 0
for c in C:
    if c in color_price_dict:
        # その皿の色が辞書にあるなら、その価格を合計に足す
        total_price += color_price_dict[c]
    else:
        # ないなら、P0を合計に足す
        total_price += P0

print(total_price)
