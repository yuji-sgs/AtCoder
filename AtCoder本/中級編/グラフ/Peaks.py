"""
https://atcoder.jp/contests/abc166/tasks/abc166_c
"""
N, M = map(int, input().split())
H = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)
    
ans = 0
for i in range(N):
    if len(G[i]) == 0:
        ans += 1
    elif H[i] > max(H[j] for j in G[i]):
        ans += 1
        
print(ans)
