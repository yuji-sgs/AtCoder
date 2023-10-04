"""
整数列A1,A2,...,ANが与えられます。 
この整数列のどの 2 つの要素も互いに異なるならば YES を、そうでないなら NO を出力してください。
"""
N = int(input())
A = list(map(int, input().split()))
if N == len(set(A)):
    print("YES")
else:
    print("NO")
