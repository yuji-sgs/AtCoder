"""
9×9 のマス目 A があり、各マスには 1 以上 9 以下の整数が書き込まれています。
具体的には、 A の上から i 行目、左から j 列目のマスには Ai,jが書き込まれています。
A が次の条件をすべてみたしているならば Yes を、そうでないならば No を出力してください。
- A の各行について、その行に含まれる 9 マスには 1 以上 9 以下の整数がちょうど 1 個ずつ書き込まれている。
- A の各列について、その列に含まれる 9 マスには 1 以上 9 以下の整数がちょうど 1 個ずつ書き込まれている。
-A の行を上から 3 行ずつ 3 つに分け、同様に列も左から 3 列ずつ 3 つに分ける。 これによって A を 9 つの 3×3 のマス目に分けたとき、それぞれの 3×3 のマス目には 1 以上 9 以下の整数がちょうど 1 個ずつ書き込まれている。
"""
A = [list(map(int, input().split())) for _ in range(9)]
Flag = True

# 行のチェック
for i in range(9):
    if len(set(A[i])) != 9:
        Flag = False
        break
    
# 列のチェック
for i in range(9):
    if len(set([A[j][i] for j in range(9)])) != 9:
        Flag = False
        break

# 3×3のマス目のチェック
for i in range(3):
    for j in range(3):
        if len(set([A[i*3+k][j*3+l] for k in range(3) for l in range(3)])) != 9:
            Flag = False
            break
        
print("Yes" if Flag else "No")
