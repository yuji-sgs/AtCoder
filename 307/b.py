"""
英小文字のみからなる N 個の文字列S1,S2,…,SNが与えられます。
1 以上 N 以下の 相異なる 整数 i,j であって、SiとSjをこの順に連結した文字列が回文となるようなものが存在するか判定してください。
ただし、長さ M の文字列 T が回文であるとは、任意の 1≤i≤M について、T の i 文字目と (M+1−i) 文字目が一致していることをいいます。
"""
N = int(input())
S = [input() for i in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            kaibun = S[i] + S[j]
            if kaibun == kaibun[::-1]:
                print("Yes")
                exit()

print("No")        
