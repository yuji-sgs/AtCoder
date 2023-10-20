"""
https://atcoder.jp/contests/abc068/tasks/arc079_a
"""
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    
voyage1 = G[0]
for v in voyage1:
    if N-1 in G[v]:
        print("POSSIBLE")
        exit()
        
print("IMPOSSIBLE")
