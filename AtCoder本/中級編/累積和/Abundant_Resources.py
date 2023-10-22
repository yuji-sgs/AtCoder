"""
https://atcoder.jp/contests/nikkei2019-final/tasks/nikkei2019_final_a
"""
N = int(input())
A = list(map(int, input().split()))

# 累積和
sum_A = [0] * (N + 1)
for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]
    
for i in range(N):
    ans = 0
    for j in range(N-i):
        ans = max(ans, sum_A[j+i+1] - sum_A[j])
        
    print(ans)
