"""
英小文字からなる長さ N の文字列 S が与えられます。
S の空でない部分文字列であって、1 種類の文字のみからなるものの数を求めてください。 ただし、文字列として等しい部分文字列同士は、取り出し方が異なっても区別しません。
なお、S の空でない部分文字列とは、S の先頭から 0 文字以上、末尾から 0 文字以上削除して得られる文字列のうち、長さが 1 以上であるもののことをいいます。 
例えば、ab や abc は abc の空でない部分文字列ですが、ac や空文字列は abc の空でない部分文字列ではありません。
"""
from collections import defaultdict

N = int(input())
S = input()
dict_S = defaultdict(int)
ans = 0

# 連長圧縮
i = 0
while i < N:
    j = i + 1
    while j < N and S[i] == S[j]:
        j += 1
    dict_S[S[i]] = max(dict_S[S[i]], j - i)
    i = j

for key, value in dict_S.items():
    ans += value
    
print(ans)
