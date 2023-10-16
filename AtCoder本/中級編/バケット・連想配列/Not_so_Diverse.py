"""
高橋君は，N 個のボールを持っています． 最初，i 番目のボールには，整数 Aiが書かれています．
高橋君は，いくつかのボールに書かれている整数を書き換えて，N 個のボールに書かれている整数が K 種類以下になるようにしたいです．
高橋君は，少なくとも何個のボールの整数を書き換える必要があるでしょうか？
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))

# バケット
kinds = [0] * 200001
for a in A:
    kinds[a] += 1   

# 0以外の種類を抽出してソート
sum_kinds = []
for i in kinds:
    if i != 0:
        sum_kinds.append(i)
sum_kinds.sort()
        
# 種類数がK以下になるまで、最小の種類をansに足し合わせる
ans = 0
for i in range(len(sum_kinds) - K):
    ans += sum_kinds[i]
    
print(ans)
