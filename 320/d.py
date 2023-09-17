"""
座標平面上に 1 から N の番号がついた N 人の人がいます。人 1 は原点にいます。
次の形式の情報が M 個与えられます。
・人Aiから見て、人Biは、x 軸正方向にXi、y 軸正方向にYi離れた位置にいる
それぞれの人がいる座標を求めてください。一意に定まらないときはそのことを報告してください。
"""
from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    A, B, X, Y = map(int, input().split())
    G[A-1].append((B-1, X, Y))
    G[B-1].append((A-1, -X, -Y))

coordinates = {}
coordinates[0] = (0, 0)

# BFS
queue = deque([0])
while queue:
    current = queue.popleft()
    cx, cy = coordinates[current]
    
    for neighbor, dx, dy in G[current]:
        nx, ny = cx + dx, cy + dy

        if neighbor in coordinates:
            continue

        else:
            coordinates[neighbor] = (nx, ny)
            queue.append(neighbor)

for i in range(N):
    if i in coordinates:
        print(f"{coordinates[i][0]} {coordinates[i][1]}")
    else:
        print("undecidable")
