"""
整数列 A=(A1,A2,…,AN) があります。 あなたは次の操作を好きな回数（0 回でもよい）行うことができます。
・1≤i,j≤N を満たす整数 i,j を選ぶ。Aiを 1 減らし、Ajを1 増やす。
A の最小値と最大値の差を 1 以下にするために必要な最小の操作回数を求めてください。
"""
N = int(input())
A = list(map(int, input().split()))
sum = sum(A)
A.sort()
B = [sum // N for i in range(0, N)]
for i in range(0, sum % N):
    B[N - 1 - i] += 1
ans = 0
for i in range(0, N):
    ans += abs(A[i] - B[i])
print(ans // 2)
