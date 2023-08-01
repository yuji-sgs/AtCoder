"""
N 行 N 列のマス目が与えられます。上から i 行目、左から j 列目のマスには整数 A i,jが書かれています。
ここで、Ai,jは 0 か 1 であることが保証されます。
マス目の外側のマスに書かれた整数を時計回りに 1 個ずつずらしたときのマス目を出力してください。
ただし外側のマスとは、1 行目、N 行目、1 列目、N 列目のいずれか 1 つ以上に属するマスの集合のことを指します。
"""
N = int(input())
A = [list(input()) for _ in range(N)]
B = [[0] * N for _ in range(N)]

for i in range(0, N):
    for j in range(0, N):
        
        if i == 0 and j == 0: # 左上
            B[i][j] = A[i+1][j]
        elif i == 0 and j-1 >= 0: # 上辺
            B[i][j] = A[i][j-1]
        elif i == 0 and j == N-1: # 右上
            B[i][j] = A[i][j-1]
        elif j == N-1 and i-1 >= 0: # 右辺
            B[i][j] = A[i-1][j]
        elif i == N-1 and j == N-1: # 右下
            B[i][j] = A[i-1][j]
        elif i == N-1 and j+1 < N: # 下辺
            B[i][j] = A[i][j+1]
        elif i == N-1 and j == 0: # 左下
            B[i][j] = A[i][j+1]
        elif j == 0 and i+1 < N: # 左辺
            B[i][j] = A[i+1][j]
        else:
            B[i][j] = A[i][j]
            
# 結果の出力
for row in B:
    print("".join(str(x) for x in row))
