"""
高橋君が 100 階建てのビルにいます。
高橋君は 2 階分までの上り、または、3 階分までの下りであれば移動には階段を使い、そうでないときエレベーターを使います。
高橋君が X 階から Y 階への移動に使うのは階段ですか？
"""
X, Y = map(int, input().split())
if (Y-X) > 2 or (X-Y) > 3:
    print("No")
else:
    print("Yes")
