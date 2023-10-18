"""
高橋くんはある文字列 s を持っています。文字列を短く表現することに興味のある高橋くんは、以下の圧縮方法を試してみることにしました。
1. 文字列 s を同じ文字が連続する文字列に分割します。（分割）
2. 分割された各文字列を、文字と、その文字が連続する長さをつなげた新たな文字列に変換します。（変換）
3. 最後に、変換した各文字列を前から順に結合します。（結合）
あなたには文字列 s が与えられるので、上記の方法で圧縮された文字列を求めるプログラムを、高橋くんの代わりに書いてください
"""
s = input()
len_s = len(s)
split = []

# 分割
i = 0
while i < len_s:
    j = i + 1
    while j < len_s and s[i] == s[j]:
        j += 1
    split.append(s[i:j])
    i = j
    
# 変換
ans = []
for i in range(len(split)):
    change = split[i][0] + str(len(split[i]))
    ans.append(change)
    
# 結合
print(''.join(ans))
