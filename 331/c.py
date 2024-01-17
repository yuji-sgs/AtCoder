"""
長さ N の数列 A=(A1,…,AN) が与えられます。
i=1,…,N のそれぞれについて次の問題を解いてください。
問題：A の要素のうち Aiより大きな要素全ての和を求めよ。
"""
# 二分探索で Ai より大きい最初の要素の位置を見つける
def binary_search_modified(A, key):
    left = 0
    right = N

    while left < right:
        mid = (left + right) // 2

        if A[mid] > key:
            right = mid
        else:
            left = mid + 1

    return right

def solve_problem(N, A):
    sorted_A = sorted(A)
    # 累積和を計算
    cum_sum = [0] * (N + 1)
    for i in range(N):
        cum_sum[i + 1] = cum_sum[i] + sorted_A[i]

    ans = []
    for a in A:
        # 二分探索で Ai より大きい最初の要素の位置を見つける
        index = binary_search_modified(sorted_A, a)
        # Ai より大きい要素の和を計算
        ans.append(cum_sum[N] - cum_sum[index])

    return ans


N = int(input())
A = list(map(int, input().split()))

print(*solve_problem(N, A))
