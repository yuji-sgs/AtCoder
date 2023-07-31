"""
N 人のスポーツ選手がいます。
N 人の選手たちには互いに相性の悪い選手のペアが M 組あり、相性の悪い組のうち i (1≤i≤M) 組目はAi番目の選手と Bi番目の選手です。
あなたは、選手を T チームに分けます。 どの選手もちょうど一つのチームに属さなければならず、どのチームにも少なくとも一人の選手が属さなければなりません。
さらに、どの i=1,2,…,M についても、Ai番目の選手と Bi番目の選手が同じチームに属していてはいけません。
この条件を満たすチーム分けの方法は何通りあるか求めてください。 
ただし、チーム分けの方法が異なるとは、ある二人が存在して、彼らが一方のチーム分けでは同じチームに所属し、もう一方では異なるチームに所属することをいいます。
"""
from collections import defaultdict

N, T, M = map(int, input().split())
g = defaultdict(list) # 隣接リスト
mod = 10**9+7 
for _ in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

color = [0]*N

def dfs(v, c):
    color[v] = c
    for u in g[v]:
        if color[u] == c or (color[u] == 0 and not dfs(u, -c)):
            return False
    return True

pow2 = [1]
for _ in range(N):
    pow2.append(pow2[-1]*2%mod)

cnt = 0
for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            print(0)
            exit(0)
        cnt += 1

print((pow2[cnt]-T)%mod)
