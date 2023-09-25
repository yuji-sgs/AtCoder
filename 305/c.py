"""
問題文省略
https://atcoder.jp/contests/abc305/tasks/abc305_c
"""
H, W = map(int, input().split())
board = [input() for _ in range(H)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

for i in range(H):
    for j in range(W):
        count = 0
        for di in range(4):
            ny = i + dy[di]
            nx = j + dx[di]
            
            if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == "#":
                count += 1
                
            if board[i][j] == "." and count >= 2:
                print(i+1, j+1)
                break
