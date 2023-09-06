"""
長いので割愛
https://atcoder.jp/contests/abc314/tasks/abc314_c
"""
N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

ans = [""] * N
tmp = {}

# 各グループに属するインデックスを集める
for i, v in enumerate(C):
    if v not in tmp: 
        tmp[v] = []
    tmp[v].append(i)

# グループごとに文字をシフト
for j in range(1, M + 1):
    if j in tmp:
        index = tmp[j]
        for k in range(len(index)):
            ans[index[k]] = S[index[k - 1]]
            if k == len(index) - 1:
                ans[index[0]] = S[index[k]]

print("".join(ans))
