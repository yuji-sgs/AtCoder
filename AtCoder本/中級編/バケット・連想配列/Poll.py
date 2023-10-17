"""
N 枚の投票用紙があり、i (1≤i≤N) 枚目には文字列 Siが書かれています。
書かれた回数が最も多い文字列を全て、辞書順で小さい順に出力してください。
"""
from collections import defaultdict
N = int(input())
vote = defaultdict(int)
for i in range(N):
    S = input()
    vote[S] += 1
  
# 書かれた回数が最も多い文字列をansに格納  
max_value = max(vote.values())
ans = []
for key, value in vote.items():
    if value == max_value:
        ans.append(key)
        
# 辞書順で小さい順に出力
ans = sorted(ans)
for a in ans:
    print(a)
