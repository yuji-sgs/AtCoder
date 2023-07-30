"""
英大文字からなる長さ 3 の文字列 S が与えられます。
S が ACE、BDF、CEG、DFA、EGB、FAC、GBD のいずれかと等しいとき Yes を、そうでないとき No を出力してください。
"""
S = input()
if S in ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]:
    print("Yes")
else:
    print("No")
