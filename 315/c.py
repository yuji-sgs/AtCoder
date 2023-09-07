"""
N カップのアイスクリームがあります。i カップ目の味はFi、美味しさはSi(Siは偶数 ) です。
あなたは、N 個のカップの中から 2 つを選んで食べることにしました。
このときの満足度は次のように定義されます。
食べたアイスクリームの美味しさを s,t ( 但し、s≥t ) とする。
2 つのカップの味が異なるなら、満足度は s+t である。
そうでないなら、満足度はs+t/2である。
満足度として達成可能な最大値を求めてください。
"""
N = int(input())
ice = []
for i in range(N):
    F, S = map(int, input().split())
    ice.append([F, S])
    
# 美味しい順にソート
ice.sort(key=lambda x:x[1], reverse=True)
max_ice_1 = ice[0]
ice.remove(ice[0])

max_ice_2 = 0
for i in range(N-1):
    # 同じ味のアイスだった場合
    if ice[i][0] == max_ice_1[0]:
        ice[i][1] = ice[i][1] // 2
    max_ice_2 = max(max_ice_2, ice[i][1])

print(max_ice_1[1] + max_ice_2)
