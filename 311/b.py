"""
1 から N までの番号がついた N 人の人がいます。
N 人の人の今後 D 日間の予定が与えられます。
人 i の予定は長さ D の文字列Siで表されて、Siの j 文字目が o ならば j 日目は暇であることを、x ならばそうでないことを意味します。
D 日間のうち全員が暇であるような 連続する 何日かを選ぶことを考えます。
選べる日数は最大で何日ですか？ただし、選べる日が存在しない場合は 0 日と答えてください。
"""
N, D = map(int, input().split())
S = [input() for _ in range(N)]

# 全員が暇な日を調べて、その連続した日数を記録
max_days = 0
count = 0

for d in range(D):
    if all(S[i][d] == 'o' for i in range(N)): # 縦方向全てoなら
        count += 1
    else:
        max_days = max(max_days, count)
        count = 0

# 最後の日が暇な日だった場合も考慮
max_days = max(max_days, count)

print(max_days)
