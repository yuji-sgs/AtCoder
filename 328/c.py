"""
英小文字のみからなる長さ N の文字列 S=S1S2…SNが与えられます。
また、S に関する Q 個の質問が与えられます。 
i=1,2,…,Q について、i 番目の質問は 2 つの整数 li,riで表される下記の質問です。
- S のli文字目からri文字目までからなる部分文字列SliSli+1…Sriにおいて、 同じ英小文字が 2 つ隣りあう箇所は何個ありますか？ すなわち、li≤p≤ri−1 かつ Sp=Sp+1を満たす整数 p は何個ありますか？
Q 個の質問それぞれの答えを出力してください。
"""
N, Q = map(int, input().split())
S = input()
S_sum = [0] * (N+1)
for i in range(N-1):
    if S[i] == S[i+1]:
        S_sum[i+1] = S_sum[i] + 1
    else:
        S_sum[i+1] = S_sum[i]

for i in range(Q):
    l, r = map(int, input().split())
    ans = 0
    print(S_sum[r-1] - S_sum[l-1])
