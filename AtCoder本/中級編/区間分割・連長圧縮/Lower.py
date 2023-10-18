"""
左右一列に N 個のマスが並んでいます。
左から i 番目のマスの高さはHiです。
あなたは好きなマスに降り立ち、右隣のマスの高さが今居るマスの高さ以下である限り右隣のマスへ移動し続けます。
最大で何回移動できるでしょうか。
"""
N = int(input())
H = list(map(int, input().split()))
move = []

i = 0
while i < N:
    j = i + 1
    cnt = 0
    while j < N and H[i] >= H[j]:
        i = j
        j += 1
        cnt += 1
    move.append(cnt)
    i = j
    

print(max(move))
