"""
1 から N までの番号が付いた N 人のプレイヤーが総当たり戦をしました。
この総当たり戦で行われた試合全てについて、二人の一方が勝ち、もう一方が負けました。

総当たり戦の結果は N 個の長さ N の文字列S1,S2,…,SNによって以下の形式で与えられます。
- i=j のとき、Siの j 文字目は o, x のいずれかであり、o のときプレイヤー i がプレイヤー j に勝ったことを、x のときプレイヤー i がプレイヤー j に負けたことを意味する。
- i=j のとき、Siの j 文字目は - である。

総当たり戦で勝った試合数が多いほうが順位が上であり、勝った試合数が同じ場合は、プレイヤーの番号が小さいほうが順位が上となります。 
N 人のプレイヤーの番号を順位が高い順に答えてください。
""" 
N = int(input())
S = [input() for _ in range(N)]
rank = []
score = [[0, i] for i in range(N)]

for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            score[i][0] += 1
        else:
            score[j][0] += 1

score = sorted(score, key = lambda x:(-x[0], x[1]))
for i in range(N):
    rank.append(score[i][1] + 1)
    
print(*rank)
