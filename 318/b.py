"""
座標平面上に N 枚の長方形のシートが張られています。
各シートが覆う長方形領域の各辺はそれぞれ x 軸または y 軸と平行であり、具体的には、i 枚目のシートはちょうどAi≤x≤BiかつCi≤y≤Diをみたす領域全体を覆っています。
1 枚以上のシートによって覆われている領域 の面積を S とすると、S は制約の条件下で整数となる事が証明できます。
S を整数の形で出力してください。
""" 
N = int(input())
board = [[False] * 101 for _ in range(101)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    for x in range(A, B):
        for y in range(C, D):
            board[x][y] = True
            
cnt = 0
for x in range(101):
    for y in range(101):
        if board[x][y]:
            cnt += 1
            
print(cnt)
