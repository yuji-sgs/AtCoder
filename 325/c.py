"""
H 行 W 列のマス目の上に 0 個以上のセンサが配置されています。
上から i 行目、左から j 列目のマス目を (i,j) と表記します。
センサが配置されているマス目の情報は長さ W の文字列 S1,S2,…,SHによって与えられ、Siの j 文字目が # のとき、またそのときに限り (i,j) にセンサが配置されています。
このセンサは上下左右斜めに隣接しているマス目に存在する他のセンサと連動し、一つのセンサとして動作します。 
また、センサ A とセンサ B が連動し、センサ A とセンサ C が連動しているとき、センサ B とセンサ C も連動することに注意してください。
連動するセンサを一つのセンサと見なしたとき、このマス目の上にあるセンサの個数を求めてください。
"""
from collections import deque

# 幅優先探索
def bfs(sy, sx):
    # 最初にスタート地点をキューに入れる
    q = deque()
    q.append((sy, sx))
    seen[sy][sx] = True
    
    while len(q) > 0:
        now = q.popleft()
        y, x = now

        for di in range(8):
            ny = y + dy[di]
            nx = x + dx[di]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if S[ny][nx] == ".":
                continue
            if not seen[ny][nx] and S[ny][nx] == "#":
                q.append((ny, nx))
                seen[ny][nx] = True
        

H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 8方向への移動ベクトル
dy = (-1, -1, -1, 0, 0, 1, 1, 1)
dx = (-1, 0, 1, -1, 1, -1, 0, 1)

seen = [[False] * W for _ in range(H)]
count = 0

for i in range(H):
    for j in range(W):
        if not seen[i][j] and S[i][j] == "#":
            bfs(i, j)
            count += 1 
            
print(count)
