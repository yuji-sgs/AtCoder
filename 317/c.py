"""
ある地方に、1 から N の番号がついた N 個の街と、1 から M の番号がついた M 本の道路があります。
i 番目の道路は街Aiと街Bjを双方向に結び、長さは C iです。
好きな街からスタートして同じ街を二度以上通らずに別の街へ移動するときの、通る道路の長さの和としてありえる最大値を求めてください。
"""
# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, input().split())
    G[A-1].append((B-1, C))
    G[B-1].append((A-1, C))

def dfs(v, total_dist):
    seen[v] = True
    max_dist = total_dist
    
    for nv, nw in G[v]:
        if not seen[nv]:
            max_dist = max(max_dist, dfs(nv, total_dist + nw))
    
    seen[v] = False # バックトラック
    return max_dist

ans = 0
for i in range(N):
    seen = [False] * N
    ans = max(ans, dfs(i, 0))
    
print(ans)
