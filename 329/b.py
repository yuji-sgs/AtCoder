"""
N 個の整数 A1,A2,…,ANが与えられます。 このうち最大でない整数の中で最大である整数を求めてください。
ただし、この問題の制約下で答えは必ず存在します。
""" 
N = int(input())
A = list(map(int, input().split()))
set_A = set(A)
set_A.remove(max(A))
print(max(set_A))
