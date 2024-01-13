"""
英大文字からなる文字列 S が与えられます。
S の各文字を空白で区切り、その順で 1 文字ずつ出力してください。
"""
S = input()
ans = ""

for i in range(len(S)):
    ans += S[i] + " "
    
print(ans[0:-1])
