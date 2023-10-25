"""
https://atcoder.jp/contests/past202104-open/tasks/past202104_d
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 累積和
Sum_A = [0] * (N + 1)
for i in range(N):
    Sum_A[i + 1] = Sum_A[i] + A[i]
    
for x in range(N - K + 1):
    print(Sum_A[x+K] - Sum_A[x])
