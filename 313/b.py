"""
長いので割愛
https://atcoder.jp/contests/abc313/tasks/abc313_b
"""
N, M = map(int, input().split())

# 最強になるうる人
Top = [True] * N

# 最強ではない人をFalseにする
for i in range(M):
    A, B = map(int, input().split())
    Top[B-1] = False

# 最強になるうる人の番号
ans = []

# 最強になるうる人の番号を追加
for i in range(N):
    if Top[i] == True:
        ans += [i+1]

# 最強になるうる人が1人の場合はその番号を出力（そうでない場合は-1を出力）
if len(ans) == 1:
    print(ans[0])
else:
    print(-1)
