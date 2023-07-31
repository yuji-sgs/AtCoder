"""
高橋君は、レストランで「AtCoder ドリンク」というドリンクを飲もうとしています。
AtCoder ドリンクは定価である P 円を払えば飲むことができます。
また、高橋君は割引券を持っており、それを使うと AtCoder ドリンクを定価より安い価格である Q 円で飲むことができますが、 その場合には AtCoder ドリンクの他に、N 品ある料理の中から 1 つを追加で注文しなければなりません。 
i=1,2,…,N について、i 番目の料理の価格は Di円です。
高橋君がドリンクを飲むため支払う合計金額の最小値を出力してください。
"""
N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

min_D = min(D)
if P < min_D + Q:
    print(P)
else:
    print(min_D + Q)


"""
頭の良い人の解答
# 入力
N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

# 定価で買った場合(P)と、
# 料理の中から1番安いものを追加で注文した場合(Q+min(D))を
# 比較して安いほうを出力する

print(min(P, Q+min(D)))
"""
