"""
英小文字からなる長さ N の文字列 S が与えられます。 
この文字列を一箇所で切断して、文字列 X と Y に分割します。
このとき、「X と Y のどちらにも含まれている文字」の種類数を最大化したいです。
文字列を切断する位置を適切に決めた際の「X と Y のどちらにも含まれている文字」の種類数の最大値を求めてください。
"""
N = int(input())
S = input()
max_num = 0
for i in range(1, N):
    X = S[:i]
    Y = S[i:]
    max_num = max(max_num, len(set(X) & set(Y)))
    
print(max_num)
