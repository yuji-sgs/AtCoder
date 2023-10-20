"""
https://atcoder.jp/contests/typical90/tasks/typical90_bz
"""
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    
ans = 0
for i in range(N):
    count = 0
    for j in G[i]:
        if i > j:
            count += 1
            
    if count == 1:
        ans += 1
        
print(ans)
