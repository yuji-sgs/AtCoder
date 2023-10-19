"""
https://atcoder.jp/contests/past202005-open/tasks/past202005_e?lang=ja
"""
N, M, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    
c = list(map(int, input().split()))
for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x = s[1]
        x -= 1
        print(c[x])
        for j in G[x]:
            c[j] = c[x]
    elif s[0] == 2:
        x, y = s[1], s[2]
        x -= 1
        print(c[x])
        c[x] = y
