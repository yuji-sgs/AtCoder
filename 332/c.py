"""
AtCoder 社はグラスとマグカップを販売しています。
高橋君は容量が G ml のグラスと、容量が M ml のマグカップを 1 つずつ持っています。
ここで、G,M は G<M をみたします。
最初、グラスとマグカップはいずれも空です。
以下の操作を K 回繰り返した後で、グラスとマグカップに水がそれぞれ何 ml ずつ入っているか求めてください。
- グラスが水で満たされているとき、すなわちグラスにちょうど G ml 入っているとき、グラスの水をすべて捨てる。
- そうでなく、マグカップが空であるとき、マグカップを水で満たす。
- 上のいずれでもないとき、マグカップが空になるかグラスが水で満たされるまで、マグカップからグラスに水を移す。
""" 
K, G, M = map(int, input().split())
Glass, Magcap = 0, 0
for i in range(K):
    if Glass == G:
        Glass = 0
    elif Magcap == 0:
        Magcap = M
    else:
        needed = G - Glass
        if Magcap > needed:
            Glass += needed
            Magcap -= needed
        else:
            Glass += Magcap
            Magcap = 0

print(Glass, Magcap)
