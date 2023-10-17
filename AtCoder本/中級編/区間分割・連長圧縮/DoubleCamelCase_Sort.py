"""
文字列 S が与えられる。これは、1 つ以上の単語を (間に空白などを挟まずに) 連結したものである。
ここで、各単語は 2 文字以上であり、最初の文字と最後の文字のみが英大文字、それ以外の文字は全て英小文字である。
これらの単語を辞書順に並べ (大文字小文字の違いは無視する)、同様に連結して出力するプログラムを作成せよ。
"""
S = input()
ans = []
i = 0
while i < len(S):
    j = i + 1
    while i < len(S) and S[j].islower():
        j += 1
    ans.append(S[i:j+1])
    i = j + 1

ans = sorted(ans, key=lambda x:x.lower())
print(''.join(ans))
