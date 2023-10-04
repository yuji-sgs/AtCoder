"""
くじ引きを N 回行い、i 回目には種類が文字列 Siで表される景品を手に入れました。
何種類の景品を手に入れましたか？
"""
from collections import defaultdict
N = int(input())
dict = defaultdict(int)

for i in range(N):
    S = input()
    dict[S] = 1
    
print(len(dict))



"""
別解（set型）
N = int(input())
S = [input() for _ in range(N)]
S = set(S)

print(len(S))
"""
