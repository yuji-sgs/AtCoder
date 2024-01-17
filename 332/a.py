"""
AtCoder 社は、オンラインショップでグッズを販売しています。
高橋君はそこで N 種類の商品を購入することにしました。
1 以上 N 以下の整数 i について、i 種類目の商品は 1 個Pi円で、高橋君はQi個購入します。
また、高橋君は送料を支払う必要があります。
送料は購入する商品の合計金額が S 円以上なら 0 円、そうでないならば K 円です。
高橋君が支払う金額は購入する商品の合計金額と送料の和です。
高橋君が支払う金額を求めてください。
"""
N, S, K = map(int, input().split())
fee = 0
for i in range(N):
    P, Q = map(int, input().split())
    fee += P * Q
    
if fee >= S:
    print(fee)
else:
    fee += K
    print(fee)
