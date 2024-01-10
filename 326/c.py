"""
高橋くんは数直線上に N 個のプレゼントを置きました。そのうち i 個目のプレゼントは座標Aiに置かれました。
あなたは数直線上の長さ M の半開区間 [x,x+M) を選び、そこに含まれるプレゼントを全て獲得します。
より詳しくは、以下の手順でプレゼントを獲得します。
- まず、実数 x をひとつ選択する。
- その後、プレゼントのうち置かれている座標が x≤Ai<x+M を満たすものを全て獲得する。
最大でいくつのプレゼントを獲得することができますか?
"""
def binary_search(key):
    left = 0
    right = N

    while left < right:
        mid = (left + right) // 2
        if A[mid] >= key:
            right = mid
        else:
            left = mid + 1

    return left

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
max_count = 0

for i in range(N):
    count = binary_search(A[i] + M) - i
    max_count = max(max_count, count)
    
print(max_count)
