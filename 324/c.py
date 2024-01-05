"""
高橋君は英小文字からなる文字列 T を青木君に向けて送りました。その結果、青木君は英小文字からなる文字列 T′を受信しました。
T'は T から一部が変更されてしまっている可能性があり、具体的には、下記の 4 つのうちのちょうど 1 つが成り立つことがわかっています。
- T′は、T と等しい。
- T′は、T のいずれか 1 つの位置（先頭と末尾も含む）に英小文字を 1 つ挿入して得られる文字列である。
- T′は、T からある 1 文字を削除して得られる文字列である。
- T′は、T のある 1 文字を別の英小文字に変更して得られる文字列である。
青木君が受信した文字列 T′と、英小文字からなる N 個の文字列S1,S2,…,SNが入力として与えられるので、 S1,S2,…,SNのうち、高橋君が送った文字列 
T と等しい可能性があるものをすべて求めてください。
"""
# 入力される整数Nと文字列Tを受け取る
N, T = input().split()
N = int(N)
ans = []

# N回ループを回して、各T'をチェックする
for i in range(N):
    T_dash = input()  # T'を入力として受け取る
    
    # 条件1と4: T'とTの長さが等しい場合
    if len(T_dash) == len(T):
        # 条件1: T'とTが完全に一致している場合
        if T_dash == T:
            ans.append(i + 1)
        # 条件4: T'とTが1文字だけ異なる場合
        else:
            diff_count = sum([s != t for s, t in zip(T_dash, T)])
            if diff_count == 1:
                ans.append(i + 1)
    
    # 条件2: T'がTに1文字を挿入したものである場合
    elif len(T_dash) - len(T) == 1:
        # ケース1: T'の最後に文字が挿入された場合
        if T_dash[:-1] == T:
            ans.append(i + 1)
            continue
        # ケース2: T'の途中に文字が挿入された場合
        for j in range(len(T)):
            if T_dash[j] != T[j]:
                if T_dash[j + 1:] == T[j:]:
                    ans.append(i + 1)
                break
    
    # 条件3: T'がTから1文字を削除したものである場合
    elif len(T) - len(T_dash) == 1:
        # ケース1: Tの最後の文字が削除された場合
        if T[:-1] == T_dash:
            ans.append(i + 1)
            continue
        # ケース2: Tの途中の文字が削除された場合
        for j in range(len(T_dash)):
            if T[j] != T_dash[j]:
                if T[j + 1:] == T_dash[j:]:
                    ans.append(i + 1)
                break

# 条件を満たすT'の数と、それらのインデックスを出力
print(len(ans))
ans.sort()
print(*ans, sep=" ")
