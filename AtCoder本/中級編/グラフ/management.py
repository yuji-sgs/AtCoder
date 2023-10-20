"""
https://atcoder.jp/contests/abc163/tasks/abc163_c
"""
N = int(input())
G = [[] for _ in range(N)]
A = list(map(int, input().split()))
for i in range(1, N):
    G[A[i-1]-1].append(i)
    
for i in range(N):
    print(len(G[i]))
