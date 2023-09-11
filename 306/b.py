"""
0 と 1 からなる長さ 64 の数列 A=(A0,A1,…,A63) が与えられます。
A0*2^0+A1*2^1+⋯+A63*2^63を求めてください。
"""
A = list(map(int, input().split()))
ans = 0

for i in range(64):
    ans += A[i] * (2 ** i)
    
print(ans)
