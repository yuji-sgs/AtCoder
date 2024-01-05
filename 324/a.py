"""
N 個の整数 A1,A2,…,ANが与えられます。
これらの値がすべて等しいならば Yes 、そうでなければ No と出力してください。
"""
N = int(input())
A = list(map(int, input().split()))
Flag = True

for i in range(1, N):
    if A[0] != A[i]:
        Flag = False
        break

print("Yes" if Flag else "No")
