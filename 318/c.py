"""
高橋君は N 日間の鉄道旅行を計画しています。高橋君はそれぞれの日について、運賃の通常料金を払うか、
1 日周遊パスを 1 枚使用するか選ぶことができます。
ここで、1≤i≤N について、i 日目の旅行にかかる運賃の通常料金はFi円です。
一方、1 日周遊パスは D 枚セットで P 円で発売されており、何セットでも購入することが可能ですが、D 枚単位でしか購入することができません。
また、購入したパスは 1 枚ずつ好きな日に使うことができ、旅行が終了した時点で余っていても構いません。
N 日間の旅行でかかる金額、すなわち 1 日周遊パスの購入にかかった代金と、1 日周遊パスを利用しなかった日における運賃の通常料金の合計金額の和としてあり得る最小値を求めてください。
"""
N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)

for left in range(0, N, D):
    right = min(left + D, N)
    cost = sum(F[left:right])
    if cost > P:
        for i in range(left, right):
            F[i] = 0
        F[left] = P
    else:
        break
ans = sum(F)
print(ans)
