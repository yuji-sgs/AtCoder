"""
https://atcoder.jp/contests/abc122/tasks/abc122_c
"""
N, Q = map(int, input().split())
S = input()

# 累積和
S_sum = [0] * (N+1)
for i in range(N):
    S_sum[i+1] = S_sum[i] + S[i-1:i+1].count("AC") # S[i-1:i+1] は S[i-1] と S[i] の間の文字列から, "AC" の数を数える

for q in range(Q):
    l, r = map(int, input().split())
    print(S_sum[r] - S_sum[l]) 
