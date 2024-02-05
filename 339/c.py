"""
一台のバスが走っています。バスの乗客の数は常に非負整数です。
このバスにはある時点で 0 人以上の乗客が乗っており、その時点から現在までに N 回停車しました。
このうち i 回目の停車では乗客が差し引き Ai人増えました。
Aiは負の値であることもあり、その場合は乗客が差し引き−Ai人減ったことを意味しています。また、停車時以外には乗客の乗り降りはありませんでした。
与えられた情報に矛盾しない現在のバスの乗客の数として考えられる最小値を求めてください。
"""
# 入力の受け取り
N = int(input())
A = list(map(int, input().split()))

# 乗客数の変動を追跡
current_passengers = 0
min_passengers = 0

for a in A:
    current_passengers += a
    # 乗客数が負になる場合、それを補正する最小乗客数を更新
    if current_passengers < 0:
        min_passengers = min(min_passengers, current_passengers)

# 最小乗客数を負にならないように調整
result = sum(A) + abs(min_passengers)

# 結果の出力
print(result)
