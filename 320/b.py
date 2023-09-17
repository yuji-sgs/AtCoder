"""
文字列 S が与えられます。 
S の連続する部分文字列のうち、回文であるものの長さの最大値を求めてください。
ただし、S の連続する部分文字列であって回文であるものは常に存在します。
""" 
def is_palindrome(s):
    return s == s[::-1]

S = input()
n = len(S)
max_len = 1

for i in range(n):
    for j in range(i+2, n+1):
        sub_str = S[i:j]
        if is_palindrome(sub_str):
            max_len = max(max_len, j-i)

print(max_len)
