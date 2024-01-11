"""
英小文字からなる長さ N の文字列 S が与えられます。
S の中で a と b が隣接する箇所があれば Yes を、なければ No を出力してください。(a と b の順序は問いません。)
"""
N = int(input())
S = input()
Flag = False

for i in range(N-1):
    if S[i] == "a" and S[i+1] == "b" or S[i] == "b" and S[i+1] == "a":
        Flag = True
        break
    
print("Yes" if Flag else "No")
