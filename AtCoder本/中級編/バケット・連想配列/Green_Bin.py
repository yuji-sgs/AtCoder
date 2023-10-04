"""
文字列 a に含まれる文字を何らかの順序で並べることで得られる文字列を a の アナグラム と呼びます。
例えば、greenbin は beginner のアナグラムです。このように、同じ文字が複数回現れるときはその文字をちょうどその回数だけ使わなければなりません。
N 個の文字列s1,s2,…,sNが与えられます。それぞれの文字列は長さが 10 で英小文字からなり、またこれらの文字列はすべて異なります。
二つの整数 i,j (1≤i<j≤N) の組であって、siがsjのアナグラムであるようなものの個数を求めてください。

◎tips
・文字列をソートする → sorted()
・文字列が何個あるか？ → 連想配列を使う（defaultdict(int)）
・n個の中から2個を選ぶ組み合わせの数 → n * (n - 1) // 2
"""
from collections import defaultdict

N = int(input())
ans = 0
dict = defaultdict(int)

for i in range(N):
    S = input()
    S = sorted(S)
    S = "".join(S)
    dict[S] += 1
    
for s in dict:
    # 文字列sがn個ある
    n = dict[s]
    ans += n * (n - 1) // 2
    
print(ans)
