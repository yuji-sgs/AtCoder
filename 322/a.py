"""
A, B, C からなる長さ N の文字列 S が与えられます。
S の中で ABC が(連続な)部分文字列として初めて現れる位置を答えてください。すなわち、以下の条件を全て満たす整数 n のうち最小のものを答えてください。
- 1≤n≤N−2
- S の n 文字目から n+2 文字目までを取り出して出来る文字列は ABC である。
ただし、ABC が S に現れない場合は -1 を出力してください。
"""
N = int(input())
S = input()
ans = 0
for i in range(0, N-2):
    if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
        ans = i+1
        break

if ans == 0:
    print(-1)
else:
    print(ans)
