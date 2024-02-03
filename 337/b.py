"""
拡張 A 文字列、拡張 B 文字列、拡張 C 文字列および拡張 ABC 文字列を以下のように定義します。
- 文字列 S が拡張 A 文字列であるとは、S のすべての文字が A であることをいいます。
- 文字列 S が拡張 B 文字列であるとは、S のすべての文字が B であることをいいます。
- 文字列 S が拡張 C 文字列であるとは、S のすべての文字が C であることをいいます。
- 文字列 S が拡張 ABC 文字列であるとは、ある拡張 A 文字列 SA、拡張 B 文字列 SB、拡張 C 文字列 SCが存在して、SA,SB,SCをこの順に連結した文字列が S と等しいことをいいます。
例えば、ABC や A 、AAABBBCCCCCCC などは拡張 ABC 文字列ですが、ABBAAAC 、BBBCCCCCCCAAA などは拡張 ABC 文字列ではありません。 
空文字列は拡張 A 文字列でも拡張 B 文字列でも拡張 C 文字列でもあることに注意してください。
A, B, C からなる文字列 S が与えられます。 S が拡張 ABC 文字列ならば Yes を、そうでなければ No を出力してください。
""" 
def is_extended_abc_string(s):
    if not s:
        return "Yes"

    # 'A' の後に 'B' が来ること、'B' の後に 'C' が来ることを確認
    prev = ""
    for char in s:
        if char < prev:
            return "No"
        prev = char

    return "Yes"

# テスト入力
S = input()
result = is_extended_abc_string(S)
print(result)
