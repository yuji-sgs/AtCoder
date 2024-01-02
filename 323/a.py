"""
0 と 1 からなる長さ 16 の文字列 S が与えられます。
2 以上 16 以下のすべての偶数 i について S の i 文字目が 0 ならば Yes を、 そうでないならば No を出力してください。
"""
S = input()
Flag = True

for i in range(len(S)):
    if (i+1) % 2 == 0 and S[i] == "1":
        Flag = False
        
print("Yes" if Flag else "No")
