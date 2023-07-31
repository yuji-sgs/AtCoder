"""
AtCoder 商店には N 個の商品があります。i (1≤i≤N) 番目の商品の価格はPiです。 
i (1≤i≤N) 番目の商品はCi個の機能をもち、i (1≤i≤N) 番目の商品の j (1≤j≤Ci) 番目の機能は 1 以上 M 以下の整数Fi,jとして表されます。
高橋くんは、AtCoder 商店の商品で一方が一方の上位互換であるものがないか気になりました。 
i 番目の商品と j 番目の商品 (1≤i,j≤N) であって、次の条件をすべて満たすものがあるとき Yes と、ないとき No と出力してください。
・ Pi≥Pjである。
・ j 番目の製品は i 番目の製品がもつ機能をすべてもつ。
・ Pi>Pjであるか、j 番目の製品は i 番目の製品にない機能を 1 つ以上もつ。
"""
N, M = map(int, input().split())

# 各商品の情報を格納するリスト
products = []
for i in range(N):
    info = list(map(int, input().split()))
    P = info[0]
    C = info[1]
    F = set(info[2:]) 
    products.append((P, C, F))
    
Flag = False

# 各商品ペアについて上位互換が存在するかをチェック
for i in range(N):
    for j in range(N):
        
        # 商品価格
        P_i = products[i][0]
        P_j = products[j][0]
        
        # 商品機能数
        C_i = products[i][1]
        C_j = products[j][1]
        
        # 商品機能の詳細
        F_i = products[i][2]
        F_j = products[j][2]

        if P_i >= P_j and F_i <= F_j: # 部分集合は<=で判定できる
            if P_i > P_j or C_j > C_i:
                Flag = True
                
if Flag:
    print("Yes")
else:
    print("No")
