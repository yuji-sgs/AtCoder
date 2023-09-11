"""
長さ N の英小文字からなる文字列 S が与えられます。
S のi 文字目をSiと記します。
S1,S1,S2,S2,…,SN,SNをこの順に連結した長さ 2N の文字列を出力してください。
"""
N = int(input())
S = input()
ans = ""

for i in range(N):
    ans += S[i]
    ans += S[i]
    
print(ans)
