"""
N 頂点 N 辺の有向グラフがあります。
i 番目の辺は頂点i から 頂点Aiに伸びます。 (i=Aiであることは制約より保証されます )
同一頂点を複数回含まない有向閉路をひとつ求めてください。
なお、この問題の制約下で答えが存在することが示せます。

◎注釈
この問題では、有向閉路とは以下の条件を全て満たす頂点の列 B=(B1,B2,…,BM) であるとします。
・ M≥2
・ BiからBi+1に辺が伸びている。(1≤i≤M-1)
・ BMからB1に辺が伸びている。
・ i≠jならばBi≠Bj

◎入力
N A1 A2 … AN
 
◎出力
M B1 B2 … BM
"""
    
N = int(input())
A = list(map(int, input().split()))

# 0-indexedに変換
A = [a-1 for a in A]

visited = [-1] * N  # 訪問済み頂点を追跡（-1は未訪問を示す）
order = []  # 訪問頂点の順序を追跡
cur = 0  # 現在の頂点

while True:
    if visited[cur] != -1: # 有向閉路が見つかった場合
        loop = order[visited[cur]:]  # 有向閉路を取得
        print(len(loop))  
        print(*[i+1 for i in loop])# 1-indexedに戻して出力
        break
    else:
        order.append(cur) # 訪問順に追加
        visited[cur] = len(order) - 1 # 訪問順を記録
        cur = A[cur]  # 次の頂点に移動
