"""
https://atcoder.jp/contests/typical90/tasks/typical90_j
"""
N = int(input())
C1 = [0] * N
C2 = [0] * N
for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        C1[i] = P
    elif C == 2:
        C2[i] = P

C1_sum = [0] * (N+1)
C2_sum = [0] * (N+1)
for i in range(N):
    C1_sum[i+1] = C1_sum[i] + C1[i]
    C2_sum[i+1] = C2_sum[i] + C2[i]
    
Q = int(input())
for q in range(Q):
    L, R = map(int, input().split())
    print(C1_sum[R] - C1_sum[L-1], C2_sum[R] - C2_sum[L-1])
