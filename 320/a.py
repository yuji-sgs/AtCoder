"""
正整数 A,B が与えられます。
A^B+B^Aの値を出力してください。
"""
A, B = map(int, input().split())
print(A ** B + B ** A)
